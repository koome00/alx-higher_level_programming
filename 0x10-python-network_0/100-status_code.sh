#!/bin/bash
# displays status code after taking a url
curl -o /dev/null -w '%{http_code}' -sLI "$1"
