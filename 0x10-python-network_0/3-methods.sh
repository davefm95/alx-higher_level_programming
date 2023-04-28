#!/bin/bash
#retrueves optioms
curl -sI -X OPTIONS "$1" | grep "Allow:" | sed 's/Allow: //'
