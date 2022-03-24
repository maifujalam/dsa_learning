read x
read y
if [ $x -gt $y ];then
  echo "X is greater then Y"
elif [ $x -lt $y ];then
  echo "X is less then Y"
else
  echo "X is equal to Y"
fi