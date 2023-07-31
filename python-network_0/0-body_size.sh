#!/bin/bash
# body size
# Check if the URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send the request using curl and get the size of the response body in bytes
response_size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the response body in bytes
echo "$response_size"