#!/bin/bash
# Display the size of body in byte

curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n'
