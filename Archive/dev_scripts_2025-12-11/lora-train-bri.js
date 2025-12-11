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
const TRAINING_DIR = path.resolve(__dirname, '..', 'lora_training', 'bri');
const OUTPUT_DIR = TRAINING_DIR;

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
║   LORA Training & Generation (fal.ai)            ║
║   Training: Bri                                   ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
${colors.reset}`);

// Validate API key
if (!FAL_KEY) {
  console.error(`${colors.red}Error: FAL_KEY not found in environment variables${colors.reset}`);
  process.exit(1);
}

// Configure fal.ai client
fal.config({
  credentials: FAL_KEY,
});

// Get all training images
async function getTrainingImages() {
  console.log(`\n${colors.cyan}${colors.bright}Step 1: Collecting training images${colors.reset}`);
  console.log(`${colors.dim}Directory: ${TRAINING_DIR}${colors.reset}`);

  const files = await fs.readdir(TRAINING_DIR);
  const imageFiles = files.filter(f => f.toLowerCase().endsWith('.png'));

  console.log(`${colors.green}✓ Found ${imageFiles.length} PNG images${colors.reset}`);

  return imageFiles.map(filename => path.join(TRAINING_DIR, filename));
}

// Upload images to FAL.ai
async function uploadImages(imagePaths) {
  console.log(`\n${colors.cyan}${colors.bright}Step 2: Uploading images to FAL.ai${colors.reset}`);

  const uploadedUrls = [];

  for (let i = 0; i < imagePaths.length; i++) {
    const imagePath = imagePaths[i];
    const filename = path.basename(imagePath);

    console.log(`${colors.yellow}Uploading ${i + 1}/${imagePaths.length}: ${filename}${colors.reset}`);

    try {
      const imageBuffer = await fs.readFile(imagePath);
      const uploadUrl = await fal.storage.upload(imageBuffer);
      uploadedUrls.push(uploadUrl);
      console.log(`${colors.green}✓ Uploaded: ${filename}${colors.reset}`);
    } catch (error) {
      console.error(`${colors.red}✗ Failed to upload ${filename}: ${error.message}${colors.reset}`);
    }
  }

  console.log(`${colors.green}✓ Uploaded ${uploadedUrls.length}/${imagePaths.length} images${colors.reset}`);
  return uploadedUrls;
}

// Train LORA model
async function trainLora(imageUrls) {
  console.log(`\n${colors.cyan}${colors.bright}Step 3: Training LORA model${colors.reset}`);
  console.log(`${colors.dim}This may take several minutes...${colors.reset}`);

  try {
    const result = await fal.subscribe('fal-ai/flux-lora-fast-training', {
      input: {
        images_data_url: imageUrls,
        trigger_word: 'BRI_PERSON',
        steps: 1000,
        learning_rate: 4e-4,
        rank: 16,
      },
      logs: true,
      onQueueUpdate: (update) => {
        if (update.status === 'IN_PROGRESS') {
          const lastLog = update.logs?.[update.logs.length - 1];
          if (lastLog?.message) {
            console.log(`${colors.yellow}${lastLog.message}${colors.reset}`);
          }
        }
      },
    });

    console.log(`${colors.green}${colors.bright}✓ LORA model trained successfully!${colors.reset}`);
    console.log(`${colors.dim}Model URL: ${result.diffusers_lora_file.url}${colors.reset}`);

    return {
      success: true,
      loraUrl: result.diffusers_lora_file.url,
      configUrl: result.config_file?.url,
    };
  } catch (error) {
    console.error(`${colors.red}✗ Training failed: ${error.message}${colors.reset}`);
    return { success: false, error: error.message };
  }
}

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
      fs.unlink(filepath).catch(() => {});
      reject(err);
    });
  });
}

// Generate images with trained LORA
async function generateWithLora(loraUrl, prompts) {
  console.log(`\n${colors.cyan}${colors.bright}Step 4: Generating new images with trained LORA${colors.reset}`);

  const results = [];

  for (let i = 0; i < prompts.length; i++) {
    const { description, prompt, filename } = prompts[i];

    console.log(`\n${colors.yellow}Generating ${i + 1}/${prompts.length}: ${description}${colors.reset}`);

    try {
      const result = await fal.subscribe('fal-ai/flux-lora', {
        input: {
          prompt: prompt,
          loras: [
            {
              path: loraUrl,
              scale: 1,
            }
          ],
          image_size: {
            width: 1024,
            height: 1024,
          },
          num_inference_steps: 28,
          num_images: 1,
          enable_safety_checker: true,
        },
        logs: true,
        onQueueUpdate: (update) => {
          if (update.status === 'IN_PROGRESS') {
            const lastLog = update.logs?.[update.logs.length - 1];
            if (lastLog?.message) {
              console.log(`${colors.dim}${lastLog.message}${colors.reset}`);
            }
          }
        },
      });

      if (result.images && result.images.length > 0) {
        const imageUrl = result.images[0].url;
        const outputPath = path.join(OUTPUT_DIR, filename);

        console.log(`${colors.green}✓ Image generated${colors.reset}`);
        console.log(`${colors.dim}Downloading...${colors.reset}`);

        await downloadImage(imageUrl, outputPath);

        console.log(`${colors.green}${colors.bright}✓ Saved: ${filename}${colors.reset}`);

        results.push({
          success: true,
          filename,
          path: outputPath,
          description,
        });
      } else {
        throw new Error('No images returned from API');
      }
    } catch (error) {
      console.error(`${colors.red}✗ Failed to generate ${description}: ${error.message}${colors.reset}`);
      results.push({
        success: false,
        filename,
        description,
        error: error.message,
      });
    }
  }

  return results;
}

// Main execution
async function main() {
  try {
    // Step 1: Get training images
    const imagePaths = await getTrainingImages();

    if (imagePaths.length === 0) {
      console.error(`${colors.red}Error: No training images found${colors.reset}`);
      process.exit(1);
    }

    // Step 2: Upload images
    const imageUrls = await uploadImages(imagePaths);

    if (imageUrls.length === 0) {
      console.error(`${colors.red}Error: No images uploaded successfully${colors.reset}`);
      process.exit(1);
    }

    // Step 3: Train LORA
    const trainingResult = await trainLora(imageUrls);

    if (!trainingResult.success) {
      console.error(`${colors.red}Error: LORA training failed${colors.reset}`);
      process.exit(1);
    }

    // Step 4: Generate new images
    const prompts = [
      {
        description: 'Business casual feminine - Professional blouse',
        prompt: 'Professional photograph of BRI_PERSON wearing a nice feminine casual blouse and professional pants, business casual style, clean modern office background, natural lighting, professional photography, high quality, feminine styling, symmetrical composition',
        filename: 'bri_business_casual_feminine_01.png',
      },
      {
        description: 'Business casual feminine - Smart casual outfit',
        prompt: 'Professional photograph of BRI_PERSON in smart business casual feminine attire with nice blouse and slacks, relaxed professional environment, soft natural lighting, high quality portrait, feminine professional style, symmetrical composition',
        filename: 'bri_business_casual_feminine_02.png',
      },
      {
        description: 'Business casual feminine - Cardigan outfit',
        prompt: 'Professional photograph of BRI_PERSON wearing a feminine cardigan with nice blouse and professional pants, warm business casual style, natural office setting, professional photography, feminine elegant styling, symmetrical composition',
        filename: 'bri_business_casual_feminine_03.png',
      },
      {
        description: 'Casual feminine - Everyday style',
        prompt: 'Casual photograph of BRI_PERSON in comfortable feminine everyday clothing, relaxed casual outfit, natural outdoor setting, soft daylight, high quality portrait, approachable feminine style, symmetrical composition',
        filename: 'bri_casual_feminine_01.png',
      },
      {
        description: 'Casual feminine - Relaxed outfit',
        prompt: 'Casual photograph of BRI_PERSON wearing relaxed feminine casual wear, comfortable everyday style, natural environment, warm natural lighting, high quality portrait, friendly casual feminine look, symmetrical composition',
        filename: 'bri_casual_feminine_02.png',
      },
    ];

    const generationResults = await generateWithLora(trainingResult.loraUrl, prompts);

    // Final summary
    console.log(`\n${colors.bright}${colors.green}=== LORA Training & Generation Complete ===${colors.reset}\n`);

    console.log(`${colors.cyan}Training Summary:${colors.reset}`);
    console.log(`  Training images: ${imagePaths.length}`);
    console.log(`  Uploaded successfully: ${imageUrls.length}`);
    console.log(`  LORA model: ${colors.green}✓ Trained${colors.reset}`);
    console.log(`  Model URL: ${colors.dim}${trainingResult.loraUrl}${colors.reset}`);

    console.log(`\n${colors.cyan}Generation Summary:${colors.reset}`);
    const successful = generationResults.filter(r => r.success).length;
    const failed = generationResults.filter(r => !r.success).length;
    console.log(`  ${colors.green}✓ Successful: ${successful}${colors.reset}`);
    if (failed > 0) {
      console.log(`  ${colors.red}✗ Failed: ${failed}${colors.reset}`);
    }

    console.log(`\n${colors.cyan}Generated Images:${colors.reset}`);
    generationResults.filter(r => r.success).forEach(r => {
      console.log(`  ${colors.green}✓${colors.reset} ${r.filename}`);
      console.log(`    ${colors.dim}${r.description}${colors.reset}`);
    });

    console.log(`\n${colors.cyan}Output Directory: ${colors.reset}${OUTPUT_DIR}\n`);

    // Save summary to file
    const summary = {
      timestamp: new Date().toISOString(),
      training: {
        images_count: imagePaths.length,
        uploaded_count: imageUrls.length,
        model_url: trainingResult.loraUrl,
      },
      generation: {
        total: generationResults.length,
        successful: successful,
        failed: failed,
        images: generationResults.filter(r => r.success).map(r => ({
          filename: r.filename,
          description: r.description,
          path: r.path,
        })),
      },
    };

    const summaryPath = path.join(OUTPUT_DIR, 'lora_training_summary.json');
    await fs.writeFile(summaryPath, JSON.stringify(summary, null, 2));
    console.log(`${colors.green}✓ Summary saved to: ${summaryPath}${colors.reset}\n`);

  } catch (error) {
    console.error(`\n${colors.red}${colors.bright}Fatal Error:${colors.reset}`, error.message);
    console.error(error.stack);
    process.exit(1);
  }
}

// Run
main().catch(error => {
  console.error(`\n${colors.red}${colors.bright}Unhandled Error:${colors.reset}`, error);
  process.exit(1);
});
