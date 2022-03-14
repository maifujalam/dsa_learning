for((i=1;i<=10;i++));
do
  aa=$((i % 2))
  if [ $aa -eq 1 ]
  then
    echo $i
  fi
done
