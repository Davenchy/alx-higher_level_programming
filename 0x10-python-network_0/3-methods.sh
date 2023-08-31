#!/bin/bash
# Get all allowed methods from the server for a url using curl
curl -sIX OPTIONS "$1" | grep Allow: | sed 's/^[aA]llow: //'
