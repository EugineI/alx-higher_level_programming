#!/bin/bash
#DELETErequest
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | cut -d " " -f2-
