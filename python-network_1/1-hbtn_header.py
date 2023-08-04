#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])
