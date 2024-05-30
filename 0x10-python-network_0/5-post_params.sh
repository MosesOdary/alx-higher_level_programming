#!/bin/bash
# Take a URL, send a POST request to the URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
