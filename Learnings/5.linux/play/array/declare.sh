#!/bin/bash
ar[1]="dd"
ar[9]="99"
echo ${ar[*]}

b=(a,2,3,4,"dd")
echo ${b[*]}

declare -a c
c[0]="0"
c[1]="1"
c[2]=2
echo ${c[*]}