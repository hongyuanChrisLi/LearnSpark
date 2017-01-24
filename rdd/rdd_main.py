import common.basic as basic
import common.two_rdd as two_rdd
import common.actions as actions
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

word_counts = basic.word_count_rdd(lines)
avg_counts = actions.avg_by_agg(basic.extract_values(word_counts))
print ("The average count value: " + str(round(avg_counts, 2)))
