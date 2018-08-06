# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Splidertest1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mName = scrapy.Field()
    pass

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # //*[@id="content"]/h1/span[1]
    name = scrapy.Field()
    #//*[@id="interest_sectl"]/div[1]/div[2]/strong
    score = scrapy.Field()
    #//*[@id="link-report"]/span[1]/span/text()[1]
    about = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    size = scrapy.Field()
    update = scrapy.Field()
    introduction = scrapy.Field()
    url = scrapy.Field()
    pass

class urlItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()

class Image(scrapy.Item):
    IMG_URL = scrapy.Field()
    IMG_PATH = scrapy.Field()