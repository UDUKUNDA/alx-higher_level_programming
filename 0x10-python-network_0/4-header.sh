#!/bin/bash
# This will send a GET request to the URL, and displays the body of the response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
