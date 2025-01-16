#!/bin/bash
#GET request curl -s -o /tmp/response_body -w "%{http_code}" "$1"
curl -sL -w "%{http_code}" "$1" -o /tmp/response_body | [ "$(cat)" -eq 200 ] && cat /tmp/response_body
