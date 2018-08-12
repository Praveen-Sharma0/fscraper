# -*- coding: utf-8 -*-
#import scrapy
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html

class MonsterbotSpider(scrapy.Spider):
    name = 'monsterbot'
    allowed_domains = ['https://www.monsterindia.com']
    start_urls = ['https://www.monsterindia.com/front-end-developer-jobs-in-bengaluru-bangalore.html/']
    
    # Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@href="javascript:void(0)"]',)), callback="parse", follow= True),)



    def parse(self, response):
        
        #Extracting the content using css selectors
        company_name=response.css(".jtxt.orange span::text").extract()
        skills = response.css('.jtxt::attr(title)').extract()
        location  = response.css(".ico1 span::text").extract()
        experience = response.css(".ico2 span::text").extract()

        #Give the extracted content row wise
        for item in zip(company_name,skills,location,experience):

            scraped_info = {
                'Company Name' :item[0],
                'Skills':item[1],
                'Location' : item[2],
                'Experience':item[3],
            }

        # next_page = response.xpath('.//a[@href="javascript:void(0)"]/@althref').extract()
        # if next_page:
        #     next_href = next_page[0]
        #     next_page_url = 'https:' + next_href
        #     request = scrapy.Request(url=next_page_url)
        #     yield request
        
            #yield or give the scraped info to scrapy
            yield scraped_info
        #pass
