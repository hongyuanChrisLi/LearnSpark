from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.core.spiders import blog_spider
import pref.setting as pref
import json
from pyspark import SparkConf, SparkContext
import copy


class PageRank:

    def __init__(self):
        data_dir = pref.get_env_variable('SPARK_DATA')
        self.file_dir = data_dir + '/blog_links.json'
        self.settings = get_project_settings()
        self.settings.set('FEED_FORMAT', 'json')
        self.settings.set('FEED_URI', self.file_dir)
        self.settings.set('LOG_LEVEL', 'INFO')
        self.link_cnt_dict = {}
        self.link_pairs = set()
        self.conf = SparkConf().setMaster('local').setAppName('My App')
        self.sc = SparkContext(conf=self.conf)

    def __craw_blog(self):
        process = CrawlerProcess(self.settings)
        process.crawl(blog_spider.BlogSpider)
        process.start()

    def __read_json(self):
        for line in open(self.file_dir, 'r'):
            # remove '[', ']' and extra ','
            # JSON file contains multiple lists
            if not(line.startswith(('[', ']'))):
                self.__parse_json(json.loads(line.rstrip('\n,')))

    def __parse_json(self, entry):
        if 'to_link' in entry:
            to_links = entry['to_link']
            from_link = entry['from_link'][0]
            for link in to_links:
                self.link_pairs.add((from_link, link))
            self.link_cnt_dict[from_link] = entry['count'][0]

    def __page_rank(self):
        link_rdd = self.sc.parallelize(self.link_pairs)
        # rdd map doesn't allow reference
        my_link_cnt_dict = copy.deepcopy(self.link_cnt_dict)
        link_pair_rdd = link_rdd.map(lambda x: (x, my_link_cnt_dict[x[0]]))

        page_rdd = link_pair_rdd.map(lambda x: (x[0][1], 1.0 / x[1]))
        page_rank_rdd = page_rdd.reduceByKey(lambda x, y: x + y).mapValues(lambda x: 0.15 + 0.85*x)
        page_rank = page_rank_rdd.sortBy(lambda x: x[1], ascending=False).collect()

        for k, v in page_rank:
            print (k + ': ' + str(v))

    def __print_elem(x):
        print(x)

    def get_report(self):
        self.__craw_blog()
        self.__read_json()
        self.__page_rank()

# Main
PageRank().get_report()
