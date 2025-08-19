import sys
k,z,r,h=sys.stdin.readline,10**9+7,range,int
k()
a=list(map(h,k().split()))
for _ in r(h(k())):
 t=tuple(map(h,k().split()))
 x,y=t[1]-1,t[2]
 m=r(x,y)
 if t[0]==1:
  for i in m:a[i]=(a[i]+t[3])%z
 elif t[0]==2:
  for i in m:a[i]=(a[i]*t[3])%z
 elif t[0]==3:a[x:y]=[t[3]]*(y-x)
 else:print(sum(a[x:y])%z)