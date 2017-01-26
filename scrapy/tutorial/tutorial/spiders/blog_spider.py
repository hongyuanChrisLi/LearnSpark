import scrapy
import re

class BlogSpider(scrapy.Spider):
    name = "blog"

    def start_requests(self):
        url = 'https://speedy-elephant.blogspot.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//a/@href').extract()
        regex = re.compile(r'speedy-elephant')
        selected_links = filter(regex.search, links)
        # print(type(links))
        # print(len(links))
        print (selected_links)