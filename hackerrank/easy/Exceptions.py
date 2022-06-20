import sys 

sys.stdin=open('input.txt')

def exception_handler(inp):
    for i in inp:
        #print(i)
        try:
            print(int(i[0])//int(i[1]))
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)
        except:
            print("Something else wrong.")


if __name__ == "__main__":
    t=int(input().strip())
    inp=[]
    for i in range(t):
        a,b=map(str,input().strip().split())
        inp.append((a,b))
    exception_handler(inp)