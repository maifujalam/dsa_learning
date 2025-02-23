#!/bin/bash
if [[ "$1" == "first" ]];then
        echo "first arg"
elif [[ "$1" == "second" ]];then
        echo "second args"
else
        echo "others"
fi
