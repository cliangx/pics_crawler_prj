# -*- coding: utf-8 -*-
import scrapy
from imgs.items import ImgsItem
import pickle
import re


class JandanSpider(scrapy.Spider):

	name = 'jandan'
	allowed_domains = ['jandan.net']
	
	with open('page_addrs.pkl', 'rb') as f:
		start_urls = pickle.load(f)
		f.close()

	def parse(self, response):
		str1 = str(response.body)
		list1 = re.findall(r'comment-4.{6}', str1)
		set1 = set(list1)
		list2 = list(set1)
		for each in list2:
			img_addr = response.xpath('//*[@id="' + each + '"]/div/div/div[2]/p/img/@src').extract()[0]
			img_url = 'http:' + img_addr
			img_name = img_url.split('/')[-1]
			
			myitem = ImgsItem()
			myitem['imgs_url'] = [img_url]
			myitem['imgs_name'] = img_name
			
			yield myitem
			