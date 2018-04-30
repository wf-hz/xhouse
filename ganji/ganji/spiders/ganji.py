import scrapy
from ..items import GanjiItem
import time

class GanJiSpider(scrapy.Spider):
	name = "SecHandHouse"
	start_urls = ['http://hz.ganji.com/fang5/']
	host_name = 'http://hz.ganji.com{}'

	def parse (self,response):
		print(response)
		gj = GanjiItem()

		# get detail data
		puid_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/@id").extract()
		title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
		model_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[1]/text()").extract()
		area_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[3]/text()").extract()
		direction_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[5]/text()").extract()
		height_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[7]/text()").extract()
		style_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[9]/text()").extract()
		address_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[3]/span/a[1]/text()").extract()
		sale_type_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[3]/span/a[2]/text()").extract()
		price_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
		price_type_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[2]/text()").extract()
		unit_price_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[2]/text()").extract()

		for a,b,c,d,e,f,g,h,i,j,k,l in zip(puid_list,title_list,model_list,area_list,\
			direction_list,height_list,style_list,address_list,sale_type_list,\
			price_list,price_type_list,unit_price_list):
			gj['puid'] = a
			gj['title'] = b
			gj['model'] = c
			gj['area'] = d
			gj['direction'] = e
			gj['height'] = f
			gj['style'] = g
			gj['address'] = h
			gj['sale_type'] = i
			gj['price'] = j
			gj['price_type'] = k
			gj['unit_price'] = l
			yield gj

		next_urls = response.xpath(".//a[@class='next']/@href").extract()
		if len(next_urls) > 0:
			next_url = self.host_name.format(next_urls[0])
			print('*******',"start to link this url :"+ next_url,'*******')
			time.sleep(0.01) # 休眠0.01秒
			# 用next_url作为参数回调parse
			yield scrapy.Request(next_url,callback=self.parse)
		else:
			pass