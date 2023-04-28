#!/bin/bash
#sends a url requaesy to a ur and displays size
curl -s -o - -w '%{size_download}\n'
