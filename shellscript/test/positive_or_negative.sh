#!/bin/bash
echo "Enter num"
read n
if [ $n -lt 0 ] ; then
    echo "Negative"
elif [ $n -eq 0 ]; then
  echo "Zero"
else
  echo "poss"
fi

