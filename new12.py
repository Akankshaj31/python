# dictionary
a = {"url1": "google.com", "url2": "demoQA.com"}  # giving key and keyvalue; key = url1, key value= google.com
b = {1: 'Akki', 2: 'Ekta'}  # key = 1, key value = ram
print(b[2])
print(a["url1"])
b[3]="moolya.com"
print(b)
print(b[3])
print(b.get(1)) #get method
print(b.keys()) #to get keys
print(b.items()) #display key with values
print(a.values()) #shows values
print(b.pop(1)) #to delete
print(a.popitem()) #to delete last item
print(a.keys())
b.update({3:"amazon.com", 4:"flipkart.com"}) #upadte method- updating key & value and multiple values at a time
print(b)
b.setdefault(5,"ekart.com") #set method for upadting key & value
print(b)
b.clear() #to clear dictionary
print(b)