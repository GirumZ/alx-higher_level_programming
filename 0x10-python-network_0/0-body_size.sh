#!/bin/bash
# A script to display size of the body in response
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
