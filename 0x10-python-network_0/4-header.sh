#!/bin/bash
# Adds header variable to display X-School-User-ID, sent value=98
curl -s -H "X-School-User-Id":98 "$1"
