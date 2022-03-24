read -p "Enter value:" c
if [[ $c == 'y' || $c == 'Y' ]]; then
  printf "YES"
elif [[ $c == 'n' || $c == 'N' ]]; then
  printf "NO"
fi