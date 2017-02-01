from pyspark import SparkConf, SparkContext
import pref.setting as pref

conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf=conf)

#dir_path = os.path.dirname(os.path.realpath(__file__))
#cwd = os.getcwd()

#print (dir_path)
#print (cwd)

data_dir = pref.get_env_variable('SPARK_DATA')
lines = sc.textFile(data_dir + '/readme.dat')
filines = lines.filter(lambda line: "guide" in line)
#filines.first()
print(filines.count())

inputRDD = sc.textFile(data_dir + '/GitHubLog.txt')
errorsRDD = inputRDD.filter(lambda line: 'ERROR' in line)
warnsRDD = inputRDD.filter(lambda line: 'WARN' in line)
badLinesRDD = errorsRDD.union(warnsRDD)

print("Num of Errors: " + str(errorsRDD.count()))
print("Num of Warns: " + str(warnsRDD.count()))
print("Num of Bad Lines: " + str(badLinesRDD.count()))

