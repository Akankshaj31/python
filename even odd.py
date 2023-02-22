list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
    print(x)
#print all odd and even number till 100 using range function
for even in range(1, 100 ):
    if even % 2 == 0:
        print(even, end=" ")
print("\n")
for odd in range(1, 100):
    if odd % 2 != 0:
        print(odd, end=" ")
#print table of 23 till 10 using range
num=24 #Store variable 24 in Num
for i in range(1, 11): #Range=1 to 10
   print(i, 'x', num, '=', i*num) # 1*24=24 ,2*24=48
#print all even and odd using only range not condition satement
#odd
for i in range(1,100,2):
    print(i,end= ' ')
print("\n")
#Even
for i in range(0,100,2):
    print(i, end=' ')
a=["java","python","html","C++"]
for x in a:
    for y in x:
        print(y,end=' ')
b="Mokshu"
for z in b:
    print(z)
list1=[["a","b","c"],["Aus","India","China","Japan"]]
for x in list1:
    for q in x:
        print(q)
list4=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
for b,c in list4:
        print("My Country is" +b+ "and I live in" +c )
#Dictionary TypeCasting
dict1=dict(list4)
print(dict1)
for m,n in dict1.items():
    print(m,n)
#Tuple Typecasting
tuple1=tuple(list4)
print(tuple1)
#Set
list5=["pen","pencil","Eraser"]
set1=set(list5)
print(set1)

n = 0
n1 = 1
print("The First Number is",n)  #n=0
print("The Second Number is",n1)#n1=1
for x in range(0,15):
    n2 = n + n1  # n2=0+1
    print(n2,end=', ')    # n2=1
    n=n1         # Here n will change n=1
    n1=n2        # Here n1 will Change n1=1
    #Again it Will Enter into For loop
    #Now n2=n+n1 ,The value is n2=1+1     1,
 #Again Print n2=2
    # Here n=n1 will change n=1
    # Here n1=n2 will Change n1=2    Fibonacci Series
