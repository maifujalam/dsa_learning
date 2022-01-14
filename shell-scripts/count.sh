#!/bin/bash
flag=true
count=0
while [ $flag ]; do
      sleep 1s
      if [ $count -eq 3 ] ; then
        flag=false
        break
      fi
      ((count++))
done
