B=[]
N=int(input('No. of elements in array B: '))
for x in range(1,N+1):
    y=int(input('Give %dth element:'%x))
    B.append(y)
print(B)
A=list(range(len(B)))
for i in range(len(B)):
    A[i]=(i+1)*B[i]-(i)*B[i-1]
print(A,'\n\n\n\n\n')