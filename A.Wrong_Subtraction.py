import math
inp=input() 
a=int(inp.split()[0])
b=int(inp.split()[1])
r=0
l=False
for i in range(b):
  if(l==False):
    r=a-i
  if(math.fmod(r,10)==0 and r!=0):
    r=r/10
    l=True
    continue
  if(math.fmod(r,10)!=0):
    r=r-1
print(int(r))
#https://codeforces.com/contest/977/problem/A #Div_3
