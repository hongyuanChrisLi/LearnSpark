import scrapy

class BlogSpider(scrapy.Spider):
    name = "blog"

    def start_requests(self):
        url = 'https://speedy-elephant.blogspot.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//a/@href').extract()
        print(type(links))
        print(len(links))
