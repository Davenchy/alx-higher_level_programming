#!/bin/bash
# send post request with data using curl
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
