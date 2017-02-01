from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.core.spiders import blog_spider
import pref.setting as pref

data_dir = pref.get_env_variable('SPARK_DATA')

settings = get_project_settings()
settings.set('FEED_FORMAT', 'json')
settings.set('FEED_URI', data_dir + '/blog_links.json')
settings.set('LOG_LEVEL', 'INFO')
process = CrawlerProcess(settings)
process.crawl(blog_spider.BlogSpider)
process.start()
