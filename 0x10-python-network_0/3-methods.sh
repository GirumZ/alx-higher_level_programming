#!/bin/bash
# A script that displays allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
