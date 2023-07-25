import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    page_number = 2
    start_urls = ["https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"]

    def parse(self, response, **kwargs):
        product_URLs = response.xpath('.//h2/a/@href').extract()

        for url in product_URLs:
            product_URL = f"https://www.amazon.in{url}"
            yield response.follow(product_URL, callback=self.parse_product_details)

        next_page = f'https://www.amazon.in/s?k=bags&page={str(AmazonSpiderSpider.page_number)}&crid=2M096C61O4MLT&qid=1690270274&sprefix=ba%2Caps%2C283&ref=sr_pg_2'

        if AmazonSpiderSpider.page_number <= 20:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_product_details(self, response):
        items = AmazonItem()
        product_name = response.css('#productTitle::text').extract()
        product_price = response.css('#corePriceDisplay_desktop_feature_div .a-price-whole::text').extract()
        number_of_reviews = response.css('#acrCustomerReviewText::text').extract()
        description = response.css('#feature-bullets .a-list-item::text').extract()
        product_description = response.css('#productDescription span , #feature-bullets .a-list-item').css(
            '::text').extract()
        ASIN = response.css('li:nth-child(4) .a-text-bold+ span::text').extract()

        manufacturer = response.css('li:nth-child(3) .a-text-bold+ span::text').extract()
        rating = response.css('#acrPopover .a-color-base::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['number_of_reviews'] = number_of_reviews
        items['product_URL'] = response.url
        items['rating'] = rating
        items['description'] = description
        items['ASIN'] = ASIN
        items['product_description'] = product_description
        items['manufacturer'] = manufacturer
        yield items
