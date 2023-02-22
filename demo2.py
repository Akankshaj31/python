a=2
print (a ** 3)
#precidance of operator
print(5-8+2)
#string manupulation
str1 ="moolya"
print(len (str1))
print(str1[4])
z=3456
c = str(z)
print(type(c))
#operations in strings
#find()
print(str1.find("l"))
print(str1.find("z"))
print(str1.upper())
print(str1)
print(str1.count("o"))
print(str1.isupper()) #checkcase
str2 = " hello "
print(str2)
print(str2.strip()) #removing space
#replace()
print(str1.replace("m","o"))
str4 ="Visakhapatnam"
print(str4)
print(str4.upper())
print(str4.replace("a","o"))
print(str2.lstrip())
print(str2.rstrip())
#method in tuple
#count
a=(1,2,3,4,5,'A','B')
print(a.count(5))
for x  in a:
    print(x)
    #print(x,end= '')


print(type(a))
b =(2,3,5,8)
z =a+b
print(z)