#!/usr/bin/env node

import * as fal from '@fal-ai/serverless-client';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables
dotenv.config();

// Configuration
const FAL_KEY = process.env.FAL_KEY;
const TRAINING_DIR = path.join(__dirname, '..', 'lora_training', 'jonathan');

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
║   HROC LORA Training (fal.ai)                    ║
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

// Upload images to fal.ai
async function uploadImages() {
  console.log(`\n${colors.cyan}${colors.bright}Step 1: Uploading training images${colors.reset}`);

  const files = await fs.readdir(TRAINING_DIR);
  const imageFiles = files.filter(f => /\.(png|jpg|jpeg|webp)$/i.test(f));

  console.log(`${colors.dim}Found ${imageFiles.length} images in ${TRAINING_DIR}${colors.reset}`);

  const uploadedUrls = [];

  for (const file of imageFiles) {
    const filePath = path.join(TRAINING_DIR, file);
    console.log(`${colors.yellow}Uploading: ${file}${colors.reset}`);

    try {
      const fileBuffer = await fs.readFile(filePath);
      const blob = new Blob([fileBuffer], { type: 'image/png' });

      const url = await fal.storage.upload(blob);
      uploadedUrls.push(url);
      console.log(`${colors.green}✓ Uploaded: ${file}${colors.reset}`);
    } catch (error) {
      console.error(`${colors.red}✗ Failed to upload ${file}: ${error.message}${colors.reset}`);
    }
  }

  return uploadedUrls;
}

// Train LORA model
async function trainLora(imageUrls) {
  console.log(`\n${colors.cyan}${colors.bright}Step 2: Training LORA model${colors.reset}`);
  console.log(`${colors.dim}Using ${imageUrls.length} images${colors.reset}`);

  try {
    const result = await fal.subscribe('fal-ai/flux-lora-fast-training', {
      input: {
        images_data_url: imageUrls.map(url => ({ url })),
        trigger_word: 'JONATHAN_HROC',
        steps: 1000,
        lora_rank: 16,
      },
      logs: true,
      onQueueUpdate: (update) => {
        if (update.status === 'IN_PROGRESS') {
          const lastLog = update.logs && update.logs.length > 0
            ? update.logs[update.logs.length - 1]?.message
            : 'Processing...';
          console.log(`${colors.yellow}Progress: ${lastLog}${colors.reset}`);
        } else if (update.status === 'IN_QUEUE') {
          console.log(`${colors.dim}Status: In Queue (Position: ${update.position || 'unknown'})${colors.reset}`);
        }
      },
    });

    console.log(`${colors.green}${colors.bright}✓ LORA training complete!${colors.reset}`);
    return result;
  } catch (error) {
    console.error(`${colors.red}✗ Error training LORA: ${error.message}${colors.reset}`);
    throw error;
  }
}

// Main execution
async function main() {
  try {
    // Step 1: Upload images
    const imageUrls = await uploadImages();

    if (imageUrls.length === 0) {
      console.error(`${colors.red}Error: No images were uploaded successfully${colors.reset}`);
      process.exit(1);
    }

    // Step 2: Train LORA
    const result = await trainLora(imageUrls);

    // Save result to file
    const resultPath = path.join(__dirname, 'lora-result.json');
    await fs.writeFile(resultPath, JSON.stringify(result, null, 2));

    console.log(`\n${colors.bright}${colors.green}=== Training Complete ===${colors.reset}\n`);
    console.log(`${colors.cyan}LORA Model Details:${colors.reset}`);
    console.log(`${colors.dim}Config URL: ${result.config_url || 'N/A'}${colors.reset}`);
    console.log(`${colors.dim}Weights URL: ${result.diffusers_lora_file?.url || 'N/A'}${colors.reset}`);
    console.log(`${colors.dim}Trigger word: JONATHAN_HROC${colors.reset}`);
    console.log(`\n${colors.cyan}Result saved to: ${resultPath}${colors.reset}\n`);

    return result;
  } catch (error) {
    console.error(`${colors.red}Fatal error: ${error.message}${colors.reset}`);
    process.exit(1);
  }
}

// Run
main().catch(console.error);
