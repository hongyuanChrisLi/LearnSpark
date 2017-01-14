import basic


def trans(func, mine,  other):
    print('------ Section ' + func.__name__ + ' ------')
    mine = func(mine, other)
    basic.word_count(mine)
    print('\n')


def union(mine, other):
    return mine.union(other)


def intersection(mine, other):
    return mine.intersection(other)
