#!/bin/bash
# Bash scipt that takes in a URL, sends request and displays size
curl -s $1 | wc -c
