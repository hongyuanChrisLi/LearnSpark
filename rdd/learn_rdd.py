from pyspark import SparkConf, SparkContext
import os
import pref.setting as pref

conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf=conf)



#dir_path = os.path.dirname(os.path.realpath(__file__))
#cwd = os.getcwd()

#print (dir_path)
#print (cwd)

data_dir = pref.get_env_variable('SPARK_DATA')
lines = sc.textFile(data_dir + '/readme.dat')
