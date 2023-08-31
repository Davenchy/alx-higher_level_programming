#!/bin/bash
# use curl to print status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
