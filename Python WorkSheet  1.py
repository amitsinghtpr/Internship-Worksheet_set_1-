#!/usr/bin/env python
# coding: utf-8

#                   **PYTHON - WORKSHEET-1**

# 1. Which of the following operators is used to calcuate remainder in a division?
# 
# Ans: C. (%)

# 2. In python 2/3 is equal to?
# 
# Ans: A.(.666)

# 3.In python, 6<<2 is equal to?
# 
# Ans:C.(24)

# 4.In python, 6&2 will give which of the following as output?
# 
# Ans:A.(2)

# 5.In python ,6|2 will give you which of the following output?
# 
# Ans: A.(2)

# 6.What does the finally keyword denoted in python?
# 
# Ans:C.(The  finally block will be executed no matter if the try block raise an error or not.)

# 7.what does raise  keyword is used for in python?
# 
# Ans:A.(It is used to raise an exception.)

# 8.Which of the following is a common use case of yeild keyword in pyhon?
# 
# Ans: C.(in defining a generator)

# **Q9 and Q10 have multiple correct answer.Choose all the correct options to answer your question.**

# 9.Which of the following are the valid variable names?
# 
# Ans: B.(1abc)

# 10. Which of the following are the keywords in python?
# 
# Ans: B.(raise)

# **Q11 and q15  are programming questions. Answer them in Jupyter Notebook.**

# 11. Write a python program  to find the factorial of a number.

# In[4]:


i=int(input("Enter number="))
fac=1
while i>0:
    fac=fac*i
    i=i-1
    
print("factorial number=",fac)


# 12.Write a python pograme to find  wheather a number is prime or composite?

# In[22]:


num=int(input("Enter any number:"))
if num> 1:
    for i in range (2,num):
        if (num % i)==0:
            print(num, "is a Composite Number")
            break
    else:
        print(num,"is a Prime number")
        

    
else:
    print(num, " is Not a prime number it us a composite number")


# In[23]:


num=int(input("Enter any number:"))
if num> 1:
    for i in range (2,num):
        if (num % i)==0:
            print(num, "is a Composite Number")
            break
    else:
        print(num,"is a Prime number")
        

    
else:
    print(num, " is Not a prime number it us a composite number")


# 13. write a python program to check wheather a given string is palindrome or not.

# In[24]:


a= input ("Enter String:")
b=a[-1::-1]
if (a==b):
    print ("Pallidrome")
else:
    print (" Not  Pallidrome")


# In[26]:


a= input ("Enter String:")
b=a[-1::-1]
if (a==b):
    print ("Pallidrome")
else:
    print (" Not  Pallidrome")


# In[27]:


get_ipython().set_next_input('14. Write a Python Program to get third side of right-angled traiangle from two given sides');get_ipython().run_line_magic('pinfo', 'sides')


# 14. Write a Python Program to get third side of right-angled triangle from two given sides?

# In[35]:


from numpy import sqrt
print ("Input Sides of traingle:")
a= float(input("Enter First Side: "))
b= float(input("Enter Second Side:"))
c= sqrt(a**2+b**2)
print("The length of Third side is",c)


# 15. Write  a python programme to print the frequecy of each of characters present in the given string?

# In[47]:


str= input ("Enter String :")

l=list(str)

freq=[l.count(ele) for ele in l]
d= dict(zip(l,freq))
print(d)


# In[ ]:




