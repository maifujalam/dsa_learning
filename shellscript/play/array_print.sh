a=(1 2 3 4 5 6 7)  # 0 based
#All elements
echo ${a[*]}
echo ${a[@]}
echo ${a[@]:0}
echo ${a[*]:0}

#Print 1st element
echo ${a}
echo ${a[0]}

#Print all elements staring 3
echo ${a[*]:3}

#print 3 to 5 all elemets
echo ${a[*]:3:2}    # echo ${ARRAYNAME[WHICH_ELEMENT]:STARTING_INDEX:COUNT_ELEMENT}

#Count array length
echo ${#a[@]}

