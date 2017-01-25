import operator


def test_pair_rdd(lines_rdd):
    words_rdd = lines_rdd.flatMap(lambda line: line.split())
    pair_rdd = words_rdd.map(lambda x: (x, 1))
    words_reduce = words_reduce_by_key(pair_rdd)
    words_reduce02 = words_reduce_by_key(words_map_values(pair_rdd))
    print_pair_rdd("Regular", words_reduce)
    print_pair_rdd("Added 1", words_reduce02)


def words_reduce_by_key(words_rdd):
    return words_rdd.reduceByKey(lambda x, y: x + y)


def words_map_values(words_rdd):
    return words_rdd.mapValues(lambda x: x + 1)


def print_pair_rdd(header, pair_rdd):
    sorted_rdd = pair_rdd.sortByKey()
    # sorted_dic = sorted_rdd.collectAsMap()
    sorted_list = sorted_rdd.take(10)

    print ("\n==== " + header + " ====\n")

    for k, v in sorted_list:
        print "%s : %s" % (str(k), str(v))
