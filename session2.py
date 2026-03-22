# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-gpulab-2025-2]
#     language: python
#     name: conda-env-conda_envs-gpulab-2025-2-py
# ---

# %% [markdown]
# # Session 2
# We are going to use notebooks for some python
# * basic types
# * flow control
#

# %% [markdown]
# Basic calculations; to change to Markdown,use esc-m, for code esc-y

# %%
1+1

# %%
1/2

# %%
a=12

# %%
a*2.5

# %%
type(a) #data types

# %%
# ?a

# %% [markdown]
# Strings:

# %%
aString="hello, 'world'"

# %%
print(aString)

# %%
aMultiline= """
Hello, world.
It is not sunny today"""

# %%
print(aMultiline)

# %%
aString.capitalize()

# %%
aString.upper()

# %%
aString.split()

# %%
aString.split("l")

# %%
aString.replace("hello","hi")

# %%
aString

# %%
aString = aString.replace("hello","hi")

# %%
aString

# %% [markdown]
# Converting data:

# %%
float(1)

# %%
a=1

# %%
b=1.2

# %%
c = str(a+b)

# %%
c+b

# %%
aString * 2

# %%
aString + aString

# %% [markdown]
# Introducing f-strings:

# %%
name = "Magnus"
age = 51

# %%
print("{0} is {1} years old".format(name, age))

# %%
print(f"{name} is {age} years old")

# %%
pi=3.14159265

# %%
print("The value of pi is {:.3f}".format(pi))

# %%
print(f"The value of pi is {pi:.3f}")

# %%
aList = []

# %%
aList.append(10)

# %%
aList.append("hello")

# %%
len(aList)

# %%
aList.append(True)

# %%
aList[2] = "world"

# %%
del aList[0]

# %%
aList

# %%
aList.remove("hello")

# %%
aList

# %%
anotherList = ["Hello", "world", "Hello"]

# %%
anotherList.remove("Hello")

# %%
anotherList

# %%
aTupe = (1,"Hello", "world") #TUPEL: not mutable

# %%
aTupe[0]= "wibble" #this will lead to an error

# %%
numbers=[1,2,3,4,5,6] # list

# %%
numbers[1:3] #inclusive, upper border exclusive

# %%
numbers[::2] #taking certain parts out of a list (start, stop, step)

# %% [markdown]
# This is slicing

# %%
#here we are reversing a list
numbers[::-1]

# %% [markdown]
# Dictionaries:

# %%
aDict  = {}

# %%
aDict["first"]= "world"

# %%
aDict["first"]

# %%
aDict[-1] =100

# %%
aDict

# %%
planets= {"Earth":1, "Jupiter": 317.8, "Mars":0.107} #also a dictionary

# %%
planets

# %%
p="Jupiter"

# %%
print(f"The mass of planet {p} is {planets[p]} earth masses") #f-string

# %%
del aDict["first"] #how to delete an entry

# %%
aDict["first"]= "world"

# %%
aDict

# %% [markdown]
# How to make a pretty dictionary

# %%
from pprint import pprint

# %%
pprint(planets)

# %% [markdown]
# i comes from matrices indexing (i,j,k)

# %%
for i in range(10):
    print (i)

# %%
aList = ["Moon", "Mars", "Jupiter"]

# %%
for x in aList:
    print (x, len(x))

# %%
for p in planets:
    print(p)

# %%
for p in planets:
    print(f"The mass of planet {p} is {planets[p]} Earth masses")

# %%
p= "Earth"

# %%
if planets[p] >1:
    print(f"{p} has a larger mass than the Earth")
elif planets [p] <1:
    print(f"{p} has a smaller mass than the Earth")
else:
    print(f"{p} has the same mass as the Earth")

# %%
for p in planets:
    if planets[p] >1:
        print(f"{p} has a larger mass than the Earth")
    elif planets [p] <1:
        print(f"{p} has a smaller mass than the Earth")
    else:
        print(f"{p} has the same mass as the Earth")

# %% [markdown]
# End of first python session.
