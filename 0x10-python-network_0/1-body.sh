#!/bin/bash
# request url using curl and print body only if status code is 200
curl -sLf "$1" || echo -n ""
