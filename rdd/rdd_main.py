import common.basic as basic
import common.two_rdd as two_rdd
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Word Count')
sc = SparkContext(conf=conf)

lines = basic.create_rdd(sc, 'recipes.dat')

# Basic Word Count Top 10
# basic.word_count(lines)

# Union and Count Top 10
# other = basic.create_rdd(sc, 'GitHubLog.txt')
# two_rdd.trans(two_rdd.union, lines, other)
# two_rdd.trans(two_rdd.intersection, lines, other)
