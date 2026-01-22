const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function scrapeLootDrop() {
  console.log('🚀 Starting scrape of loot-drop.io...');

  const browser = await chromium.launch({
    headless: true
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  // Listen for console messages
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log('Console error:', msg.text());
    }
  });

  try {
    // Navigate to the page
    await page.goto('https://www.loot-drop.io/', {
      waitUntil: 'networkidle',
      timeout: 60000
    });

    console.log('✅ Page loaded successfully');

    // Wait for initial content
    await page.waitForSelector('article', { timeout: 10000 });
    console.log('✅ Initial content loaded');

    // Get initial count
    let prevCount = 0;
    let currentCount = await page.locator('article').count();
    console.log(`📊 Initial companies loaded: ${currentCount}`);

    // Scroll to load all companies
    console.log('🔄 Starting infinite scroll to load all companies...');

    let scrollAttempts = 0;
    const maxScrollAttempts = 100;

    while (scrollAttempts < maxScrollAttempts) {
      // Scroll to bottom
      await page.evaluate(() => {
        window.scrollTo(0, document.body.scrollHeight);
      });

      // Wait for new content to load
      await page.waitForTimeout(1000);

      // Check current count
      currentCount = await page.locator('article').count();

      if (currentCount > prevCount) {
        console.log(`📊 Companies loaded: ${currentCount} (+${currentCount - prevCount})`);
        prevCount = currentCount;
        scrollAttempts = 0; // Reset counter if new content loaded
      } else {
        scrollAttempts++;
      }

      // Check if we've reached the target
      if (currentCount >= 1209) {
        console.log('✅ Reached target of 1209+ companies!');
        break;
      }

      // Safety limit
      if (scrollAttempts > 30) {
        console.log('⚠️ No new content after 30 attempts, stopping...');
        break;
      }
    }

    console.log(`\n📊 Final count: ${currentCount} companies`);

    // Extract all company data
    console.log('🔍 Extracting company data...');

    const companies = await page.evaluate(() => {
      const articles = document.querySelectorAll('article');
      const data = [];

      articles.forEach((article, index) => {
        try {
          // Get company name from heading
          const heading = article.querySelector('h2, h3, h4, [class*="name"], [class*="title"]');
          const name = heading ? heading.textContent.trim() : `Company ${index + 1}`;

          // Get description
          const description = article.textContent;

          // Get all text content for parsing
          const fullText = article.innerText;

          // Extract year (looking for patterns like "2019", "2020", etc.)
          const yearMatch = fullText.match(/\b(19|20)\d{2}\b/);
          const year = yearMatch ? yearMatch[0] : 'Unknown';

          // Extract funding burned (looking for patterns like "$275M", "$50M BURNED", etc.)
          const fundingMatch = fullText.match(/\$[\d,.]+(?:M|K|B)\s*BURNED?|\$[\d,.]+(?:M|K|B)/i);
          const funding = fundingMatch ? fundingMatch[0] : 'Unknown';

          // Get category from emoji or class
          const emojiElements = article.querySelectorAll('[class*="category"], [class*="tag"]');
          let category = 'Unknown';

          // Try to find emoji in the article
          const emojis = ['🔧', '📱', '💸', '🛒', '🪙', '🚗', '📺', '🏥', '🎮', '🌐', '📊', '🔒', '🧬', '♻️', '🎓', '💼', '🪣'];
          for (const emoji of emojis) {
            if (fullText.includes(emoji)) {
              category = emoji;
              break;
            }
          }

          // If no emoji found, try to find category from common patterns
          if (category === 'Unknown') {
            const categoryMap = {
              'HARDWARE': '🔧',
              'FINTECH': '💸',
              'SOCIAL': '📱',
              'E-COMMERCE': '🛒',
              'CRYPTO': '🪙',
              'ON-DEMAND': '🚗',
              'MEDIA': '📺',
              'HEALTH': '🏥',
              'GAMING': '🎮',
              'SAAS': '🌐'
            };

            for (const [key, value] of Object.entries(categoryMap)) {
              if (fullText.toUpperCase().includes(key)) {
                category = value + ' ' + key;
                break;
              }
            }
          }

          data.push({
            name,
            year,
            funding,
            category,
            description: fullText.trim().substring(0, 500)
          });
        } catch (e) {
          console.error(`Error parsing article ${index}:`, e);
        }
      });

      return data;
    });

    console.log(`✅ Extracted ${companies.length} companies`);

    // Generate Markdown output
    let markdown = `# Loot Drop - Dead Startups Data\n`;
    markdown += `Generated: ${new Date().toISOString()}\n`;
    markdown += `Total companies: ${companies.length}\n\n`;
    markdown += `---\n\n`;

    companies.forEach((company, index) => {
      markdown += `## ${index + 1}. ${company.name}\n\n`;
      markdown += `- **Năm đóng cửa**: ${company.year}\n`;
      markdown += `- **Funding bị đốt**: ${company.funding}\n`;
      markdown += `- **Category**: ${company.category}\n`;
      markdown += `- **Mô tả**: ${company.description}\n\n`;
      markdown += `---\n\n`;
    });

    // Save to file
    const outputPath = path.join(__dirname, 'loot-drop-data.md');
    fs.writeFileSync(outputPath, markdown, 'utf8');
    console.log(`✅ Data saved to: ${outputPath}`);

    // Also save JSON for backup
    const jsonPath = path.join(__dirname, 'loot-drop-data.json');
    fs.writeFileSync(jsonPath, JSON.stringify(companies, null, 2), 'utf8');
    console.log(`✅ JSON backup saved to: ${jsonPath}`);

    // Print summary
    console.log('\n📊 Summary:');
    console.log(`- Total companies: ${companies.length}`);
    console.log(`- Output file: ${outputPath}`);

  } catch (error) {
    console.error('❌ Error during scraping:', error);
  } finally {
    await browser.close();
    console.log('🔒 Browser closed');
  }
}

// Run the scraper
scrapeLootDrop();
