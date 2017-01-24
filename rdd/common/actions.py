import basic


# Calculate the average using aggregate action
def avg_by_agg(nums):
    val = \
        nums.aggregate((0, 0),
                       (lambda acc, value: (acc[0] + value, acc[1] + 1)),
                       (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])))
    #print(str(val[0]) + ", " + str(val[1]))

    return val[0] / float(val[1])


def test_fold(values):
    res1 = values.fold(0, lambda x, y: x + y)
    res2 = values.fold(1, lambda x, y: x + y)
    print ("res1 : " + str(res1))
    print ("res2 : " + str(res2))
