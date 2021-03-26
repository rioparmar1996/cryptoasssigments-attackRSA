import time
start=time.time()
print("Enter the public key e, n:", end='')
e=int(input())
N=int(input())
print("Enter a cipher text:", end='')
c=int(input())

factors=[]
p=[]
q=[]
x=[]
count=0

for i in range(1, N+1):
    if(N%i==0):
        factors.append(i)

for i in range(0, len(factors)):
    for j in range(0, len(factors)):
        if (factors[i]*factors[j]==N):
            p.append(factors[i])
            q.append(factors[j])
            x.append((p[i],q[i]))

for i in range(0, len(x)):
    x = (p[i]-1)*(q[i]-1)
    for j in range(1, x):
        w = j*e
        if (w % x==1):
            s=i
            d=j

m=(c**d) % N
print("p =",p[s], "\tq =",q[s], "\td =",d, "\tM =",m)

end=time.time()
print("execution time:",(end-start),"sec")
