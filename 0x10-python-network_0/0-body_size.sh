#!/bin/bash
#send request and display size ob body
curl -s -o /dev/null -w "%{size_download}\n" "$1"
