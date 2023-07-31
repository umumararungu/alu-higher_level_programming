#!/bin/bash
# body size
response_size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')
echo "$response_size"