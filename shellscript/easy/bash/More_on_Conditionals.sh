#!/bin/bash
read x
read y
read z

if [[ ($x == $y) && ($y == $z) ]];then
  printf "EQUILATERAL"
elif [[  $x == $y || $y == $z || $z == $x ]]; then
  printf "ISOSCELES"
else
  printf "SCALENE"
fi
