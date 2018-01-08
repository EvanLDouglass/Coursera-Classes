# Evan Douglass
# Parsing XML Data

# This program retrieves XML from a webpage, extracts data about comment
# counts and sums the total number of comments

from urllib.request import urlopen
import xml.etree.ElementTree as ET

# find url
url = input('Enter url - ').strip()
html = urlopen(url).read()

# get XML tree
tree = ET.fromstring(html)

# get list of comment numbers
comments = tree.findall('.//count')
nums = []
for item in comments:
    if item != None:
        num = item.text
        nums.append(int(num))

print('Total comments =', sum(nums))
