#!/bin/bash
while true; do
  v=1
  while [[ $v -lt 3600 ]];do
    v=$(($v+1))
    sleep 1
  done
done