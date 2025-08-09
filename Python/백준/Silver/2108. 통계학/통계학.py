from statistics import*
n,*a=map(int,open(0))
a.sort()
print(round(mean(a)),a[n//2],(2*multimode(a))[1],a[-1]-a[0])