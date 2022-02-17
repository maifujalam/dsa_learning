FILE=$1
echo "checking all pending csrs"
while [ true ]; do
  if [ -f "$FILE" ]; then
      echo "$FILE cluster created"
      break ;
  else
    echo "checking csr now."
     for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
  fi
  sleep 5;
done