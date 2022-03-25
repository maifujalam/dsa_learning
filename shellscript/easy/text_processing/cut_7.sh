while read line;do
  echo "$line" | cut -d ' ' -t 4
done