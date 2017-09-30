#!/bin/bash

FILES=""

cd doc

while read FILE; do
  if [ -f ${FILE} ]; then
      FILES="${FILES} ${FILE}"
  fi
done <sisallysluettelo.txt

pandoc ${FILES} -o dokumentaatio.pdf
