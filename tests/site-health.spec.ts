import { test, expect } from '@playwright/test';

const BASE_URL = process.env.SITE_URL || 'https://hrocinc.org';

const PAGES = [
  { path: '/', name: 'Homepage' },
  { path: '/bri', name: 'Bri Profile' },
  { path: '/lilly', name: 'Lilly Profile' },
  { path: '/jonathan', name: 'Jonathan Profile' },
  { path: '/documents', name: 'Documents' },
];

for (const page of PAGES) {
  test.describe(page.name, () => {
    test(`loads with HTTP 200`, async ({ request }) => {
      const response = await request.get(`${BASE_URL}${page.path}`);
      expect(response.status()).toBe(200);
    });

    test(`has no broken images`, async ({ page: browserPage }) => {
      const brokenImages: string[] = [];

      browserPage.on('response', (response) => {
        const url = response.url();
        if (/\.(webp|png|jpg|jpeg|gif|svg)(\?.*)?$/i.test(url)) {
          if (response.status() >= 400) {
            brokenImages.push(`[${response.status()}] ${url}`);
          }
        }
      });

      await browserPage.goto(`${BASE_URL}${page.path}`, {
        waitUntil: 'networkidle',
        timeout: 30000,
      });

      // Scroll to bottom to trigger any lazy-loaded images
      await browserPage.evaluate(async () => {
        const delay = (ms: number) => new Promise((r) => setTimeout(r, ms));
        for (let y = 0; y < document.body.scrollHeight; y += 400) {
          window.scrollTo(0, y);
          await delay(100);
        }
      });
      await browserPage.waitForTimeout(1000);

      expect(brokenImages, `Broken images on ${page.name}:\n${brokenImages.join('\n')}`).toHaveLength(0);
    });

    test(`has no console errors`, async ({ page: browserPage }) => {
      const errors: string[] = [];
      browserPage.on('console', (msg) => {
        if (msg.type() === 'error') {
          errors.push(msg.text());
        }
      });

      await browserPage.goto(`${BASE_URL}${page.path}`, {
        waitUntil: 'networkidle',
        timeout: 30000,
      });

      // Filter out known third-party script errors
      const realErrors = errors.filter(
        (e) =>
          !e.includes('cdn-cgi') &&         // Cloudflare-injected scripts
          !e.includes('email-decode') &&    // Cloudflare email obfuscation
          !e.includes('googletagmanager') && // GA4 (placeholder ID or ad blocker)
          !e.includes('google-analytics')   // GA4 beacon
      );

      expect(realErrors, `Console errors on ${page.name}:\n${realErrors.join('\n')}`).toHaveLength(0);
    });
  });
}

test.describe('S3 Assets', () => {
  test('all S3 image URLs are accessible', async ({ request }) => {
    // Fetch homepage and all founder pages, collect S3 image URLs
    const s3Urls = new Set<string>();

    for (const page of PAGES) {
      const response = await request.get(`${BASE_URL}${page.path}`);
      const html = await response.text();
      const matches = html.matchAll(/src="(https:\/\/[^"]*s3[^"]*\.(webp|png|jpg|jpeg|gif|svg))"/gi);
      for (const match of matches) {
        s3Urls.add(match[1]);
      }
    }

    expect(s3Urls.size).toBeGreaterThan(0);

    const broken: string[] = [];
    for (const url of s3Urls) {
      const resp = await request.head(url);
      if (resp.status() !== 200) {
        broken.push(`[${resp.status()}] ${url}`);
      }
    }

    expect(broken, `Broken S3 URLs:\n${broken.join('\n')}`).toHaveLength(0);
  });
});
