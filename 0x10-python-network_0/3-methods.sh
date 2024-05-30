#!/bin/bash
# Display all HTTP methods a server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
