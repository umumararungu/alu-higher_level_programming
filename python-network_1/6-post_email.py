#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    response = requests.post(url, data={"email": value})
    print("{}".format(response.text))
