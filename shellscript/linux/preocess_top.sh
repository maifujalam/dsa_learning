#!/usr/bin/env bash
process=$(ps aux | head -n 3)
echo $process   # Assisigned value to a variable
echo $0  # File name with full path
echo $1   # Forst parameter
echo $#  # number of parameters
echo $@  # all parameters
echo $?  # Exist status of last command
echo $$  # Process ID of current shell

arr=(a  b c)
