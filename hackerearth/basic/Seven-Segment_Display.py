import sys

sys.stdin = open('input.txt', 'r')

for _ in range(int(input().strip())):
    n = input()
    total_match = 0
    match = {'0': 6, '1': 2, '2': 5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    result=""
    for i in range(len(n)):
        total_match += match[n[i]]
    if total_match == '3':
        result='7'
    elif total_match%2==0:
        result='1'*(total_match//2)
    else:
        result='7'+'1'*((total_match-3)//2)
    print(result)