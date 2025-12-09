#!/usr/bin/env node

import * as fal from '@fal-ai/serverless-client';
import fs from 'fs/promises';
import { createWriteStream } from 'fs';
import https from 'https';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables
dotenv.config();

// Configuration
const FAL_KEY = process.env.FAL_KEY;
const IMAGE_WIDTH = parseInt(process.env.IMAGE_WIDTH) || 1920;
const IMAGE_HEIGHT = parseInt(process.env.IMAGE_HEIGHT) || 1080;
const IMAGE_QUALITY = process.env.IMAGE_QUALITY || 'high';
const NUM_IMAGES = parseInt(process.env.NUM_IMAGES) || 1;

// Output directory
const OUTPUT_DIR = path.join(__dirname, '..', 'images', 'generated');

// Colors
const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  dim: '\x1b[2m',
  cyan: '\x1b[36m',
  magenta: '\x1b[35m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
};

// Banner
console.log(`${colors.magenta}${colors.bright}
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   HROC Image Generator (fal.ai)                  ║
║   Healing Roots Outreach Collective              ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
${colors.reset}`);

// Validate API key
if (!FAL_KEY) {
  console.error(`${colors.red}Error: FAL_KEY not found in environment variables${colors.reset}`);
  console.log(`${colors.yellow}Please create a .env file with your fal.ai API key:${colors.reset}`);
  console.log('FAL_KEY=your_api_key_here\n');
  console.log(`Get your API key from: ${colors.cyan}https://fal.ai/dashboard/keys${colors.reset}`);
  process.exit(1);
}

// Configure fal.ai client
fal.config({
  credentials: FAL_KEY,
});

// Load prompts
let prompts;
try {
  const promptsData = await fs.readFile(path.join(__dirname, 'prompts.json'), 'utf8');
  prompts = JSON.parse(promptsData);
} catch (error) {
  console.error(`${colors.red}Error loading prompts.json:${colors.reset}`, error.message);
  process.exit(1);
}

// Ensure output directory exists
await fs.mkdir(OUTPUT_DIR, { recursive: true });

// Download image from URL
async function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    const file = createWriteStream(filepath);
    https.get(url, (response) => {
      response.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(filepath);
      reject(err);
    });
  });
}

// Generate single image
async function generateImage(promptData, category) {
  const { id, description, prompt, negative_prompt, filename } = promptData;

  console.log(`\n${colors.cyan}${colors.bright}Generating: ${description}${colors.reset}`);
  console.log(`${colors.dim}ID: ${id}${colors.reset}`);
  console.log(`${colors.dim}Category: ${category}${colors.reset}`);

  try {
    const result = await fal.subscribe('fal-ai/flux/dev', {
      input: {
        prompt: prompt,
        negative_prompt: negative_prompt,
        image_size: {
          width: IMAGE_WIDTH,
          height: IMAGE_HEIGHT,
        },
        num_inference_steps: IMAGE_QUALITY === 'high' ? 50 : 28,
        num_images: NUM_IMAGES,
        enable_safety_checker: true,
      },
      logs: true,
      onQueueUpdate: (update) => {
        if (update.status === 'IN_PROGRESS') {
          console.log(`${colors.yellow}Progress: ${update.logs[update.logs.length - 1]?.message || 'Processing...'}${colors.reset}`);
        }
      },
    });

    if (result.images && result.images.length > 0) {
      const imageUrl = result.images[0].url;
      const outputPath = path.join(OUTPUT_DIR, filename);

      console.log(`${colors.green}✓ Image generated successfully${colors.reset}`);
      console.log(`${colors.dim}Downloading to: ${outputPath}${colors.reset}`);

      await downloadImage(imageUrl, outputPath);

      console.log(`${colors.green}${colors.bright}✓ Saved: ${filename}${colors.reset}`);

      return {
        success: true,
        id,
        filename,
        path: outputPath,
        url: imageUrl,
      };
    } else {
      throw new Error('No images returned from API');
    }
  } catch (error) {
    console.error(`${colors.red}✗ Error generating ${description}:${colors.reset}`, error.message);
    return {
      success: false,
      id,
      error: error.message,
    };
  }
}

// Parse command line arguments
const args = process.argv.slice(2);
const options = {
  category: null,
  id: null,
  all: false,
  test: false,
};

for (let i = 0; i < args.length; i++) {
  const arg = args[i];
  if (arg === '--category' || arg === '-c') {
    options.category = args[++i];
  } else if (arg === '--id' || arg === '-i') {
    options.id = args[++i];
  } else if (arg === '--all' || arg === '-a') {
    options.all = true;
  } else if (arg === '--test' || arg === '-t') {
    options.test = true;
  } else if (arg === '--help' || arg === '-h') {
    console.log(`
${colors.bright}Usage:${colors.reset}
  node generate.js [options]

${colors.bright}Options:${colors.reset}
  -c, --category <name>    Generate all images in a category (hero, services, community, abstract)
  -i, --id <id>           Generate a specific image by ID
  -a, --all               Generate all images (use with caution!)
  -t, --test              Test mode - show available categories and IDs
  -h, --help              Show this help message

${colors.bright}Examples:${colors.reset}
  node generate.js --category hero              ${colors.dim}# Generate all hero images${colors.reset}
  node generate.js --id hero-main               ${colors.dim}# Generate specific image${colors.reset}
  node generate.js --all                        ${colors.dim}# Generate everything${colors.reset}
  node generate.js --test                       ${colors.dim}# Show available options${colors.reset}

${colors.bright}Available Categories:${colors.reset}
${Object.entries(prompts).map(([key, value]) => `  ${colors.cyan}${key}${colors.reset}: ${value.name}`).join('\n')}
`);
    process.exit(0);
  }
}

// Test mode - show available options
if (options.test) {
  console.log(`\n${colors.bright}Available Images:${colors.reset}\n`);

  for (const [categoryKey, categoryData] of Object.entries(prompts)) {
    console.log(`${colors.magenta}${colors.bright}${categoryKey.toUpperCase()}${colors.reset} - ${categoryData.name}`);
    for (const promptData of categoryData.prompts) {
      console.log(`  ${colors.cyan}${promptData.id}${colors.reset}: ${promptData.description}`);
      console.log(`    ${colors.dim}→ ${promptData.filename}${colors.reset}`);
    }
    console.log('');
  }

  console.log(`${colors.yellow}Run with --category <name> or --id <id> to generate images${colors.reset}\n`);
  process.exit(0);
}

// Main generation logic
const results = [];

if (options.all) {
  console.log(`${colors.yellow}${colors.bright}WARNING: Generating ALL images. This will use API credits!${colors.reset}`);
  console.log(`${colors.dim}Press Ctrl+C to cancel within 5 seconds...${colors.reset}\n`);
  await new Promise(resolve => setTimeout(resolve, 5000));

  for (const [categoryKey, categoryData] of Object.entries(prompts)) {
    console.log(`\n${colors.magenta}${colors.bright}=== ${categoryData.name} ===${colors.reset}`);
    for (const promptData of categoryData.prompts) {
      const result = await generateImage(promptData, categoryKey);
      results.push(result);
    }
  }
} else if (options.category) {
  const categoryData = prompts[options.category];
  if (!categoryData) {
    console.error(`${colors.red}Error: Category "${options.category}" not found${colors.reset}`);
    console.log(`${colors.yellow}Available categories:${colors.reset} ${Object.keys(prompts).join(', ')}`);
    process.exit(1);
  }

  console.log(`\n${colors.magenta}${colors.bright}=== ${categoryData.name} ===${colors.reset}`);
  for (const promptData of categoryData.prompts) {
    const result = await generateImage(promptData, options.category);
    results.push(result);
  }
} else if (options.id) {
  let found = false;
  for (const [categoryKey, categoryData] of Object.entries(prompts)) {
    const promptData = categoryData.prompts.find(p => p.id === options.id);
    if (promptData) {
      const result = await generateImage(promptData, categoryKey);
      results.push(result);
      found = true;
      break;
    }
  }

  if (!found) {
    console.error(`${colors.red}Error: Image ID "${options.id}" not found${colors.reset}`);
    console.log(`${colors.yellow}Run with --test to see available IDs${colors.reset}`);
    process.exit(1);
  }
} else {
  console.log(`${colors.yellow}No options specified. Use --help for usage information${colors.reset}`);
  console.log(`${colors.dim}Quick start: node generate.js --test${colors.reset}\n`);
  process.exit(0);
}

// Summary
console.log(`\n${colors.bright}${colors.green}=== Generation Complete ===${colors.reset}\n`);
const successful = results.filter(r => r.success).length;
const failed = results.filter(r => !r.success).length;

console.log(`${colors.green}✓ Successful: ${successful}${colors.reset}`);
if (failed > 0) {
  console.log(`${colors.red}✗ Failed: ${failed}${colors.reset}`);
}

console.log(`\n${colors.cyan}Images saved to: ${OUTPUT_DIR}${colors.reset}\n`);

if (successful > 0) {
  console.log(`${colors.bright}Next steps:${colors.reset}`);
  console.log(`1. Review generated images in: ${colors.dim}${OUTPUT_DIR}${colors.reset}`);
  console.log(`2. Move desired images to your website: ${colors.dim}../images/${colors.reset}`);
  console.log(`3. Update HTML to reference new images\n`);
}
