"""
Aaa=int(input())
Bbb=int(input())
def comp (A,B):
    C=Aaa*Bbb
    D=Aaa+Bbb
    if C>D:
        return C
    else:
        return D
print (comp(Aaa,Bbb))
"""

import sys

def print(*objects, sep=' ', end='\n'):
  text = sep.join(map(str, objects))
  sys.stdout.write(f'{text}{end}')

def input():
  return sys.stdin.readline().rstrip('\r\n')

Sec=input().split(' ')
sec=input().split(' ')
def check (Sec,sec):
    k=int(Sec[1])
    n=int(Sec[0])
    div=int(n/k)
    cont=0
    for el in range(1,n+1):
        if str(el) in sec:
            sec.remove(str(el))
        elif sec == []:
           continue
        else:
           cont+=1
    return cont
print(check(Sec,sec))
