import common.basic as basic

lines = basic.create_rdd('recipes.dat')

# Basic Word Count Top 10
basic.word_count(lines)