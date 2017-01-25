import two_rdd


def test_pair_rdd(lines_rdd):
    words_rdd = get_words_rdd(lines_rdd)
    pair_rdd = words_rdd.map(lambda x: (x, 1))
    words_reduce = words_reduce_by_key(pair_rdd)
    # words_reduce2 = words_reduce_by_key(words_map_values(pair_rdd))
    # words_reduce3 = words_count_combine_by_key(pair_rdd)
    words_reduce4 = word_list_combine_by_key(words_reduce.sortByKey())
    # print_pair_rdd("Regular", words_reduce)
    # print_pair_rdd("Added 1", words_reduce2)
    # print_pair_rdd("combineByKey", words_reduce3)
    print_pair_rdd("combineByKey", words_reduce4)


def test_two_pair_rdd(lines01, lines02):
    words01 = get_word_pairs_rdd(lines01)
    words02 = get_word_pairs_rdd(lines02)
    words12 = two_rdd.subtract_by_key(words01, words02)
    words_reduce_by_key(words12).foreach(print_elem)


def get_words_rdd(lines_rdd):
    return lines_rdd.flatMap(lambda line: line.split())


def get_word_pairs_rdd(lines_rdd):
    return get_words_rdd(lines_rdd).map(lambda x: (x, 1))


def words_reduce_by_key(words_rdd):
    return words_rdd.reduceByKey(lambda x, y: x + y)


def words_map_values(words_rdd):
    return words_rdd.mapValues(lambda x: x + 1)


def words_count_combine_by_key(pair_rdd):
    return pair_rdd.combineByKey(
        lambda x: x,
        lambda x, y: x + y,
        lambda x, y: x + y)


def word_list_combine_by_key(pair_rdd):
    keys = pair_rdd.keys()
    alpha_pair_rdd = keys.map(lambda x: (x[:1], x))

    #alpha_pair_rdd.keys().foreach(print_elem)

    return  alpha_pair_rdd.combineByKey(
        lambda x: (x, 1),
        lambda x, y: (x[0] + ", " + y, x[1] + 1),
        lambda x, y: (x[0] + ", " + y[0], x[1] + y[1])
    ).map(lambda z: (z[0], "[" + str(z[1][1]) + "] : " + z[1][0]))


def print_pair_rdd(header, pair_rdd):
    sorted_rdd = pair_rdd.sortByKey()
    # sorted_dic = sorted_rdd.collectAsMap()
    sorted_list = sorted_rdd.take(10)

    print ("\n==== " + header + " ====\n")

    for k, v in sorted_list:
        print "%s : %s" % (str(k), str(v))

def print_elem (x):
    print(x)