import basic


# Calculate the average using aggregate action
def avg_by_agg(nums):
    val = \
        nums.aggregate((0, 0),
                       (lambda acc, value: (acc[0] + value, acc[1] + 1)),
                       (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])))
    #print(str(val[0]) + ", " + str(val[1]))

    return val[0] / float(val[1])


#def test_reduce()