#Assignment 1

import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_42.json'

link = urllib.urlopen(url)
js = json.load(link)

print json.dumps(js, indent=4)
print js['comments'][2]['count']
