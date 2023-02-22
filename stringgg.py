#formatting in string
a = "my name is Akanksha."
b = "How are you?"
print("welcome!",a,b)
print("welcome!",b,a)
print("welcome! {} {}".format(a,b))
print("welcome! {1} {0}".format(a,b))
print("welcome! {about} {question}".format(about= a ,question= b))
