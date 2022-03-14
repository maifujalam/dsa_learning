#!/bin/bash
echo "Enter no"
read x
sum=0
while [ $x -gt 0 ]; do
  rem=$((x%10))
  sum=$((sum+rem))
  x=$((x/10))
done
echo $sum