#!/bin/bash
# use curl to send JSON file as a body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
