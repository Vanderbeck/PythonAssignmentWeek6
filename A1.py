#Assignment 1

import urllib
import json

url = raw_input('Enter URL: ') #'http://python-data.dr-chuck.net/comments_42.json'

link = urllib.urlopen(url)
js = json.load(link)

total =0
for u in js['comments']:
    txt = u['count']
    num = int(txt)
    total = total + num

print total

# print json.dumps(js, indent=4)
# print js['comments'][2]['count']
