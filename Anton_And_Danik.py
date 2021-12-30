t=int(input())
s=input() 
d=0
a=0
for i in range(t):
  if(s[i]=='D'):
    d=d+1
  if(s[i]=='A'):
    a=a+1
if((a>d)==True):
    print("Anton")
if((a<d)==True):
    print("Danik")
if((a==d)==True):
    print("Friendship")
