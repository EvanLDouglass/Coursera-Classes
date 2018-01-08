# Evan Douglass

# This program takes a file with integers and uses regular expressions
# to sum them

import re

# get file
fname = input('Enter file name: ')
fname = open(fname, 'r')

# find the integers in the file
nums = list()
for line in fname:
    # return all ints of any length
    line_digits = re.findall('[0-9]+', line)
    # convert to type int and add to nums
    for ints in line_digits:
        num = int(ints)
        nums.append(num)

fname.close()

print(sum(nums))
