#!/bin/bash
# request url using curl and print body only if status code is 200
curl -sf "$1" || echo -n ""
