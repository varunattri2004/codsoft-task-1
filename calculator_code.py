#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculator
a=float(input("enter the 1st number:"))
b=float(input("enter the 2nd number:"))
print("= for addition")
print("- for subtraion")
print("* for multiplication")
print("/ for division")
print("% for modulus")
print("** for exponent ")

o=input("enter the operator:")
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
elif o=="*":
    print(a*b)
elif o=="/":
    print(a/b)
elif o=="%":
    print(a%b)
elif o=="**":
    print(a**b)
else:
    print("INVALID OPTION")
    


# In[ ]:




