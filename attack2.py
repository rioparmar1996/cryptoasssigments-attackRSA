import time
start=time.time()
print("Enter the public key e, n:", end='')
e=int(input())
N=int(input())
print("Enter a cipher text:", end='')
c=int(input())
counter=0
while counter<N+1:
    a=counter**e
    if a%N==c%N:
        m=counter
    counter+=1
print("original message:",m)
end=time.time()
print("execution time:",(end-start),"sec")



