import sys 
import itertools

sys.stdin=open('input.txt')

def comb(S,n):
	for i in range(1,n+1):
		for j in list(itertools.combinations(S,i)):
			print(''.join(j))

if __name__ == '__main__':
	S,n=map(str,input().strip().split())
	n=int(n)
	S=sorted(S)
	comb(S,n)
	