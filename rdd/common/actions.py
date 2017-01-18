def sum_count(nums):
    sum_count_val = nums.aggregate((0, 0),
                                   (lambda acc, value: (acc[0] + value, acc[1] + 1),
                                    (lambda acc1, acc2: (acc1[0] + acc2[2], acc1[1] + acc2[1]))))
    return sum_count_val
