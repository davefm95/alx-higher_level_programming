#!/bin/bash
#sends a url requaesy to a ur and displays size
curl -sI "$1" | grep -i content-length | awk '{print $2}'
