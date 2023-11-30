#!/bin/bash
# A script that sends a request to a url
curl -so /dev/null -w "%{http_code}" "$1"
