#!/bin/bash
# Display the size of body in byte

curl -Is "$1" | grep  Content-Length | cut -f2 -d' '
