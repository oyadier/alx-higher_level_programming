#!/bin/bash
# he is by enablec
curl -Is "$1"| grep Allow |cut -c 8-
