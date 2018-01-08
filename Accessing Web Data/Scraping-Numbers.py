# Evan Douglass
# Scraping Numbers from HTML

# This program scrapes data from a website's HTML using Beautiful Soup
# and the url library in Python. The program sums the numbers collected.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# find url
url = input('Enter url - ').strip()
html = urlopen(url, context=ctx).read()

# get and clean HTML
soup = BeautifulSoup(html, 'html.parser')

# retrieve all span tags
tags = soup('span')

# get the numbers in each tag and output the sum
nums = [int(tag.contents[0]) for tag in tags]

print(sum(nums))
