from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.core.spiders import blog_spider


process = CrawlerProcess(get_project_settings())
process.crawl(blog_spider.BlogSpider)
process.start()
