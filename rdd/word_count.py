from pyspark import SparkConf, SparkContext
import os
import pref.setting as pref
import re
import operator

def rm_special_chars(line):
    return re.sub('[^a-zA-Z \n]', '', line)

conf = SparkConf().setMaster('local').setAppName('Word Count')
sc = SparkContext(conf=conf)

data_dir = pref.get_env_variable('SPARK_DATA')
lines = sc.textFile(data_dir + '/recipes.dat')
lines = lines.map(rm_special_chars).map(lambda line: line.lower())
words = lines.flatMap(lambda line: line.split())
word_counts = words.countByValue()
sorted_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)

for k,v in sorted_counts:
    print "%s : %s" % (str(k), str(v))