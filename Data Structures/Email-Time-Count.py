# Evan Douglass

# This program searches a text file with email information and counts
# the number of times messages are sent during each hour of the day.

# open a file
fname = input('Enter file name: ')
fname = open(fname, 'r')

# get the time and add to dictionary with a count value
hcount = dict()
for line in fname:
    if line.startswith('From '):
        lst = line.split()
        hour = lst[5].split(':')[0] # split time and select hour
        hcount[hour] = hcount.get(hour, 0) + 1

# sort dictionary by hour
hcount = sorted(hcount.items())

# output frequency of hours
for key, value in hcount:
    print(key, value)
