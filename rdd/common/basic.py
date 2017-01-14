import operator
import re
from pyspark import SparkConf, SparkContext
import pref.setting as pref

def create_rdd(filename):
    conf = SparkConf().setMaster('local').setAppName('Word Count')
    sc = SparkContext(conf=conf)
    data_dir = pref.get_env_variable('SPARK_DATA')
    lines = sc.textFile(data_dir + '/' + filename)
    lines = lines.map(rm_special_chars).map(lambda line: line.lower())
    return lines


def rm_special_chars(line):
    return re.sub('[^a-zA-Z \n]', '', line)


def word_count (lines):
    words = lines.flatMap(lambda line: line.split())
    word_counts = words.countByValue()
    sorted_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    cnt = 0
    for k, v in sorted_counts:
        print "%s : %s" % (str(k), str(v))
        cnt += 1
        if cnt > 10:
            break
