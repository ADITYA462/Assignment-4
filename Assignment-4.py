#!/usr/bin/env python
# coding: utf-8

# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# 
# 
# 
# sample input: 10
# 
# sample output: 35

# In[15]:


r = lambda a : a + 25
print(r(10))


# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# 
# 
# 
# sample list: [1, 2, 3, 4, 5, 6, 7]
# 
# 
# 
# Triple of list numbers:
# 
# [3, 6, 9, 12, 15, 18, 21]

# In[16]:


nums = (1,2,3,4,5,6,7) 
print("original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of list numbers:")
print(list(result))


# In[ ]:





# Write a Python program to square the elements of a list using map() function.
# 
# 
# 
# Sample List: [4, 5, 2, 9]
# 
# Square the elements of the list:
# 
# [16, 25, 4, 81]

# In[17]:


def square_num(n):
  return n * n
nums = [4,5,2,9]
print("sample List: ",nums)
result = map(square_num, nums)
print("Square of the elements of list:")
print(list(result))


# In[ ]:





# In[ ]:




