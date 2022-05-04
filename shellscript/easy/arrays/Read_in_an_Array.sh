#!/bin/bash
x=""
while read line; do
  x+=$line
  x+=" "
done
echo $x