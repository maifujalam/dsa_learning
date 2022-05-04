#!/bin/bash

declare -a array
while read line; do
    array+=$line
done

for i in {3..7};do
  echo ${array[i]}
done
