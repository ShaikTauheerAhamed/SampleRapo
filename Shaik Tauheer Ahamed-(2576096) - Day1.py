#!/usr/bin/env python
# coding: utf-8

# # 1.manipulating using a list
# ## 1.to add a new elements to the end of the list.
# 
# 

# In[2]:


lst=[123,345,789]
lst.append(786)
lst


# # 2.to reversse elements in the string
# 

# In[5]:


lst1=[6764,5566,789]
lst1.reverse()
print(lst1)


# # 3.To display the same list of elements mutiple times

# In[8]:


lst=[234,432,542]
lst


# In[9]:


l=lst*3
l


# # 4. To concatenate two lists

# In[10]:


lst2=[8878,563,666]
print(lst+lst2)


# # 5.To sort the elements of the list in ascending order

# In[13]:


lst.sort()
lst


# # 2.Write a pyrhon program to do in tuples

# # 1.manipulatig using tuples

# In[30]:


tuple1=(898,"tauheer",908.2)


# # 2. To add new element to the end of tuple

# In[31]:


tuple2=(85,55.3,"Ahamed")


# In[32]:


new_tuple=tuple1+tuple2
print(new_tuple)


# # 3. To reverse elements in the list

# In[35]:


tuple3=tuple1[::-1]
tuple3


# # 4.To display the elements of same tuple multiple times

# In[39]:


t=(tuple1*3)
t


# # 5.To concatanate two tuples

# In[40]:


t1=tuple1+tuple2
t1


# # 6.To sort the elements of the list in ascending order

# In[47]:


tuple3=(425,55.45,5359)
tuple3=list(tuple3)
tuple3.sort()
tuple3=tuple(tuple3)
print(tuple3)


# # 3.Wite a python program to implement the following using list

# # 1.Create a list with integers (min 10)

# In[48]:


lstt=(1,2,3,4,5,6,7,8,9,10)
lstt


# # 2.display last number in the list
# 

# In[51]:


lstt[-1]


# In[52]:


### 3.command to display values from the list [0:4]
lstt[0:4]


# In[53]:


### 4.command to display values from [2:]
lstt[2:]


# In[54]:


### 5 command to display values from [:6]
lstt[:6]


# # 4.write a pythn program :tuple1=(10,50,20,40,30)

# In[56]:


tuple1=(10,50,20,40,30)
tuple1


# In[59]:


### 1.to display elements 10 and 50 from tuple1
tuple1[0:2]


# In[62]:


### 2.to display length of tuple1
len(tuple1)


# In[63]:


### 3. to find the minimum element from tuple1
min(tuple1)


# In[71]:


### 4 To add all elements to tuple1
tuple2=(54,76)
tuple2


# In[74]:


tuple1+=tuple2
print(tuple1)


# we cant add elements to tuple because they are immutable

# In[79]:


### %.to display same tuple multiple times
print(tuple1)


# In[80]:


tuple1=(10,50,20,40,30)
tuple1*3


# # 5.write a python program 

# In[90]:


### 1.to calculate length of string
str1=["tauheer","Ahamed"]
print(str1)


# In[91]:


len(str1)


# In[101]:


### 2. to reverse words in string
txt = "TAuheerAhamed"[::-1]
print(txt)


# In[104]:


### 3. To display the same string multiple times
txt1=txt*3
print(' ' ,txt1)


# In[105]:


### 4 To concatanate two strings
txt3="Hello"
txt4="World"
txt5=txt3+txt4
print(txt5)


# In[106]:


### 5.str1="South India",using string slicing to display "india"
str1='South India'
print(str1[5:])


# # 6.perform the following

# In[118]:


### 1. Creating a directory
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# In[119]:


print(thisdict)


# In[123]:


### 2.Accessing keys and vakues in dictionary
value=thisdict["brand"]
print(value)



# In[124]:


### 3.updating dictionary using a function
dict2={
    "price": 900000,
    
}
thisdict.update(dict2)
print(thisdict)


# In[127]:


### 4.clear and delete dictionary values
dict2.clear()
print(dict2)


# # 7.Python program to insert any number in a list
# 

# In[135]:


num_list = [1, 2, 3, 4, 5]

print(f'Current Numbers List {num_list}')

num = int(input("Please enter a number to add to list:\n"))

index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))

num_list.insert(index, num)

print(f'Updated Numbers List {num_list}')


# # 8 .python program to delete an eement from a list by index

# In[136]:


num_list


# In[140]:


num_list.pop()
num_list


# # 9. Write a program to display anumber from 1 to 100
# 

# In[145]:


import random
number=random.randint(1,100)
print(number)


# # 10.write a python program to find sum of all numbers in tuple

# In[147]:


tuple5=(10,25.5,12)
sum=0
for i in tuple5:
    sum=sum+i
    i=i+1
print(sum)
    


# # 11.ceate a dictionary containing 3 lambda functions square,cube and square root
# 

# In[149]:


dict={
    "square": "",
    "cube":"function for cube",
    "square root":"function for square root"
}
print(dict)


# In[150]:


dict(value)=input("enter the square value")
print(dict)


# # 12 . A list of words is gien .find the words from the list that have there second character in upper case

# In[153]:


ls=["hello","Dear","hOw","ARe","You"]


result = [word for word in ls if len(word) > 1 and word[1].isupper()]

print(result)


# # 13 .a dictionary of names and there weights are given.Find how much they will weight on the moon

# In[156]:


weightOnMoon={
    "john":(45*1.62)/9.81,
    "Shelly":(65*1.62)/9.81
}
print(weightOnMoon)


# # control Statements
# 

# # 1 . write a python program to find the first n prime numbers

# In[163]:


i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1


# # 2.Salary calculator

# In[167]:


b_sal=int(input("enter basic salary of the employee"))
hra=int(input("Enter HRA"))
ta=int(input("Enter TA value"))
da=int(input("Enter DA value"))
g_sal=b_sal+hra+ta+da
tax=g_sal-1/10
n_sal=g_sal-tax
print("The gross salary of the employee is ", g_sal)
print("The net salary of the employee is ", n_sal)


# # 3.python program to search a string in list
# 

# In[175]:


list6=("shaik","tauheed","ahamed")
list6


# In[176]:


t1="tauheer"
if t1==list6:
    print("String found")
else:
    print("String not found")


# # 4. display number odd and even number between 12 and 37

# In[187]:


o_count=0
e_count=0
for i in range (12,37):
    
  if not i%2:
        e_count=e_count+1
  else:
        o_count=o_count+1
print("The number of odd numbers is ", +o_count)
print("The numbe of even numbers is ", +e_count)


# # 5 Python program to print sum of odd and even numbers between 12 to 37

# In[189]:


o_sum=0
e_sum=0
for i in range (12,37):
  if i%2==0:
    e_sum=e_sum+i
  else:
    o_sum=o_sum+i
print("The sum of odd numbers is ", +o_sum)
print("The sum of even numbers is ", +e_sum)


# 
# 
# # 6.Python program to print the table of any number

# In[193]:


n=int(input("Enter the table number"))
for i in range (1,11):
  print(n,"x",i,"=",n*i)


# # 7.Pyrthon program to print first 10 prime numbers

# In[194]:


i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1


# # 8.write a python program to print arthamatic operations using nested if statement

# In[195]:


# chek whether a number is a positive number
n=int(input("Entr a number "))
if n>0:
    if n==0:
        print("Negitive number")
    else:
        print("positive number")


# # 9. convert temperature from celcious to forein heat

# In[200]:


c=int(input("Enter a celcious temperature "))
f=c*4.5+32
print(f)


# # 10 functions (didnt discuss yet)

# # 11. python program to print number of seconds in 30 days
# 

# In[2]:


days=(int(input("Enter number of days ")))
hours=(int(input("Enter number of hours ")))
secs=(int(input("Enter number of seconds ")))
total=days*hours*secs
print(total)


# # 12.python program to print number od seconds in a year

# In[3]:


days=(int(input("Enter number of days ")))
hours=(int(input("Enter number of hours ")))
secs=(int(input("Enter number of seconds ")))
total=days*hours*secs
print(total)


# # 13.Calculate average speed of train
# 

# In[2]:


a_speed=int(input("Enter the average speed of train "))
distance=int(input("Enter the total distance need to travel "))
time=distance/a_speed
print("The average time taken is ",+time ,"Hours")


# # 14.print time spent in school

# In[3]:


days_in_each_school_year=192
joining_year=int(input("Enter joining year "))
ending_year=int(input("Enter ending year"))
time_spent_in_school=int(input("enter time"))
if (time_spent_in_school==6):
    y_diff=ending_year-joining_year
    h_time=y_diff*days_in_each_school_year*6
    print("Total hours spent in school is ",+h_time)


# # 15.youngest and eldest of 3

# In[4]:


a_ram=int(input("Enter ram age"))
a_sam=int(input("Enter sam age"))
a_khan=int(input("Enter khan age"))
if a_ram>a_sam:
  if a_ram>a_khan:
    print("Ram is big")
  else:
    print("khan is big")
else:
  print("Sam is big")


# # 15 this program contains functions 

# In[5]:


rows = int(input("Enter Pyramid Pattern Rows = "))

print("Pyramid Star Pattern") 

for i in range(0, rows):
   for j in range(0, rows - i - 1):
       print(end = ' ')
   for k in range(0, i + 1):
       print('*', end = ' ')
   print()


# In[10]:


# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)


# In[ ]:




