# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	# pass
	puid = scrapy.Field()
	title = scrapy.Field()
	model = scrapy.Field()
	area = scrapy.Field()
	direction = scrapy.Field()
	height = scrapy.Field()
	style = scrapy.Field()
	address = scrapy.Field()
	sale_type = scrapy.Field()
	price = scrapy.Field()
	price_type = scrapy.Field()
	unit_price = scrapy.Field()