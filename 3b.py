import string
import random
str1=string.printable
print(str1)

len=int(input("enter the length of a password:"))
b = " ".join(random.sample(str1,len))

print(b)
