#!/bin/sh
sed -i \
         -e 's/rgb(0%,0%,0%)/#16304d/g' \
         -e 's/rgb(100%,100%,100%)/#fff0e2/g' \
    -e 's/rgb(50%,0%,0%)/#16304d/g' \
     -e 's/rgb(0%,50%,0%)/#b9cef5/g' \
 -e 's/rgb(0%,50.196078%,0%)/#b9cef5/g' \
     -e 's/rgb(50%,0%,50%)/#16304d/g' \
 -e 's/rgb(50.196078%,0%,50.196078%)/#16304d/g' \
     -e 's/rgb(0%,0%,50%)/#fff0e2/g' \
	"$@"