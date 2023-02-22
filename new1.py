s={10,20,40,60,50,50,'A'} #noduplicates allowed #set is unorderd homogenious
print(s)
print(len(s))
print(50 in s)
s.add(200)
print(s)
s.pop()
print(s)
T={20,30,40,50,70}
A ={50,10,70}
Z =T.union(A)
print(Z)
B = T.symmetric_difference(A)
print(B)
C = {50,20}
print(C.issubset(T))
C.discard(50)
print(C)