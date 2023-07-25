# Scrape_amazon_products

commands to install required pakages:
  1. pip install Scrapy
  2. pip install scrapy-user-agents
  3. pip install scrapy-proxy-pool
  4. pip install scrapy-fake-useragent

To run the bot and get output in desired file:
  1. open terminal
  2. type "scrapy crawl amazon_spider -o output.csv" for output in a csv file
  3. type "scrapy crawl amazon_spider -o output.json" for output in a json file

if you can't scrape correct output, check the css selectors as amazon and many other companies changes and make updates in their websites time-to-time