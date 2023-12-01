#!/bin/bash
# Takes in URL and displaye all methods
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
