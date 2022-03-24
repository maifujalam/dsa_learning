#!/bin/bash
while read line;do
  echo $line | cut -f1-2
done