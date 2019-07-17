p1,m2=map(int,input().split())
n3=[]
t4=[]
gcd5=1
for i in range(1,p1+1):
    if(p1%i==0):
        n3.append(i)
for j in range(1,m2+1):
    if(m2%j==0):
        t4.append(j)
for y in n3:
    if y in t4:
        gcd5=gcd5*y
print(gcd5)
