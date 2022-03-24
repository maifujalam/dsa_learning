read -p "Enter filename:" file_name
while read l; do
    echo $l
done<$file_name

