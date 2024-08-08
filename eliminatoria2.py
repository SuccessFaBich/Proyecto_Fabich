"""
N=int(input())
dif=input()
exp=input()
diff=dif.split(' ')
expp=exp.split(' ')
def prob (diff,expp,N):
    bdif=0
    bexp=0
    for turn in N:
        if (int(diff[bdif])*60)/int(expp[bexp]):
""" 
"""
nums=input().split(' ')
kils=input().split(' ')
maxk=int(input())
m=int(nums[1])
n=int(nums[0])
cont=0
def waa (kils, maxk)
for cada in kils:
    if maxk >= int(cada):
        cont+=1
print (cont)
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
    for el in range(1,k+1):
        for time in range(0,div):
            if str(el) in sec:
                sec.remove(str(el))
            else:
                cont+=1
    return cont
print(check(Sec,sec))
