n=5
for (( i=0;i<n;i++)); do
  rem=$(($i % 2))
  if [ $rem == 0 ]; then
    echo $i
  fi
done

