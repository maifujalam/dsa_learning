#!/bin/bash
echo "read a"
read a
echo "enter b"
read b
echo "read c"
read c
if [ $a -gt $b ] && [ $a -gt $c ]; then
  echo $a
fi