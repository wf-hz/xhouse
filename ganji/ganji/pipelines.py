# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import mysql.connector as ms

class GanjiPipeline(object):
	def open_spider(self,spider):
		self.conn  = ms.connect(host='localhost',port=3306,user='xuser',passwd='Hello12345.',db='xhouse')
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		insert_sql = "insert into ganji_shhouse (puid,title,model,area,direction,height,style,address,sale_type,price,price_type,unit_price)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".\
			format(item['puid'],item['title'],item['model'],item['area'],item['direction'],item['height'],item['style'],item['address'],item['sale_type'],item['price'],item['price_type'],item['unit_price'])
		self.cursor.execute(insert_sql)
		# 提交到数据库执行
		self.conn.commit()
		return item

	def spider_close(self,spider):
		self.conn.close()

