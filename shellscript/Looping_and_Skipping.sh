#!/bin/bash
for((i=1;i<=99;i++))
do
  rem=$((i%2))
  if [ $rem -eq 1 ]; then
    echo $i;
  fi
done