# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    description = scrapy.Field()
    ASIN = scrapy.Field()
    manufacturer = scrapy.Field()
    product_description = scrapy.Field()
    product_URL = scrapy.Field()
    number_of_reviews = scrapy.Field()
    product_price = scrapy.Field()
    rating = scrapy.Field()
    product_name = scrapy.Field()
