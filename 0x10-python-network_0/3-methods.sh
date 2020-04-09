#!/bin/bash
# Script that send a DELETE request to the URL
curl $1 -sI | grep "Allow" | cut -d " " -f2-
