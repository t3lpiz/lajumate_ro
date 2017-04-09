# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.by import By
from ansicolor.ansicolor import red, cyan

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['lajumate.ro']
    start_urls = ['http://lajumate.ro/']

    rules = (
        Rule(LinkExtractor(allow=r'\.'), callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        i['name'] = response.xpath('//h1[@itemprop="name"]/text()').extract()
        i['description'] = response.xpath('//h1[@itemprop="description"]/text()').extract()
#        try:
#            self.browser.get(response.url)
#            WebDriverWait(driver=self.browser, timeout=10).until(EC.presence_of_element_located((By.ID, 'phone_label')))
#            nr_telefon_link = self.browser.find_element_by_id('phone_label')
#            nr_telefon_link.click()
#            nr_telefon_text = self.browser.find_element_by_id('phone_label')
#            print(nr_telefon_text.text)
#        except Exception as e:
#            print(e)
#        return i
        print(red(i['name'])
                )
        print(cyan(i['description']))
        print(response.url)
        with open('rezultat', 'a') as f:
            f.write(response.url + '\n')
            f.close()
