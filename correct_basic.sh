#!/bin/bash

if [ ! -f "$1" ] ; then
    echo "supplied file: $1 doesn't exist"
    exit 1
fi
file="$1"

sed -i -e 's/$/\\\\/' -e '/section/s/\\\\$//' $file
