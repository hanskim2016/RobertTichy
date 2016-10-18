# import the regex search/filter/replace functions
import re
# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.fool.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
#print soup.prettify() # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below
a_tags = soup.find_all("a")
# print a_tags
refs=[]
for alink in a_tags:
    # print alink,"*END*"
    a_link=str(alink)
    href = re.findall(r"href=\"(.+?)\"",a_link)
    # print href
    refs.append(href[0])
# print refs
refs.sort()
prior_key = refs[0]
times = 0
dict = {}
for each_key in refs:
    if (each_key != prior_key):
        dict[prior_key]=times
        prior_key=each_key
        times=1
    else:
        times=times+1
print dict
