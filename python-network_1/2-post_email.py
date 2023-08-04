#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """"Documented"""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
