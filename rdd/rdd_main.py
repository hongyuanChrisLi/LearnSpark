import common.basic as basic
import common.two_rdd as two_rdd
import common.actions as actions
import common.pair_rdd as pair_rdd
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Word Count')
sc = SparkContext(conf=conf)

lines01 = basic.create_rdd(sc, 'recipes.dat')
# lines02 = basic.create_rdd(sc, 'recipes02.dat')

pair_rdd.test_pair_rdd(lines01)

# Basic Word Count Top 10
# basic.word_count(lines)

# Union and Count Top 10
# other = basic.create_rdd(sc, 'GitHubLog.txt')
# two_rdd.trans(two_rdd.union, lines, other)
# two_rdd.trans(two_rdd.intersection, lines, other)

# word_counts = basic.word_count_rdd(lines)
# avg_counts = actions.avg_by_agg(basic.extract_values(word_counts))
# print ("The average count value: " + str(round(avg_counts, 2)))

# values = sc.parallelize([1, 2, 3, 4, 5], 1)
# actions.test_fold(values)
