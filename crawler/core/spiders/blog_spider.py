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
        sel_links = filter(regex.search, links)
        cln_links = [i.split('#', 1)[0] for i in sel_links]
        link_set = set(cln_links)
        print (link_set)
