#!/bin/bash

FILES=""

cd ../doc

while read file; do
  if [ -f $file ]; then
      FILES=$(echo $FILES $file)
  fi
done <sisallysluettelo.txt

pandoc $FILES -o dokumentaatio.pdf 
