#!/bin/bash
# request url using curl and print content size
curl -sI "$1" | grep Content-Length | awk '{print $2}'
