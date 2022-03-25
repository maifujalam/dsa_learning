#!/bin/bash
while read line;do
  echo "$line" | tr -s ' ' ' '
done