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
# Open data in python:

# %%
dataFile = open("data/pulse_data.csv")

# %%
# Why does this not work?
#inFile = open('dataFile','r') 
#This works only for files
#this is not a file anymore, but a variable. you have to use "data/pulse_data.csv"

# %%
# inFile = open("data/pulse_data.csv",'r') #this should work

# %% [markdown]
# Show current directory:

# %%
# !pwd #Why the exclamation mark? : Without !, Python treats pwd as a variable name

# %% [markdown]
# create an empty list:

# %%
time = []
absorption = []

# %%
dataFile.readline() #discarding first line (header)
for line in dataFile.readlines():
    line = line.split(",")
    time.append(float(line[0]))
    absorption.append(float(line[1]))

# %%
print(len(time), len(absorption))

# %% [markdown]
# Look at the first 10 values in both lists

# %%
for i in range (10):
    print (time[i], absorption [i])

# %%
import numpy
from matplotlib import pyplot

# %%
x=numpy.random.normal(size=(500,)) #normally distributed
y=numpy.random.normal(size=(500,))

# %%
pyplot.plot(x,y,"o") # "o" disconnects the lines to dots

# %%
pyplot.plot(x,y,"or")
pyplot.xlabel("x-axis")
pyplot.ylabel("y-axis")
pyplot.title("Random Points")

# %%
pyplot.plot? #explain the plot function

# %% [markdown]
# Homework session 3: plot the pulse data you loaded earlier

# %%
x=time
y=absorption

# %%
pyplot.plot(x,y) #all 63.000 datapoints

# %%
pyplot.plot(x[:1000],y[:1000],"o") # only first 1000 points, 
# use slicing ([:100]) or head(100) so that the plotting function only sees those first 100 datapoints.

# %%
pyplot.plot(x[:2000],y[:2000]) #lines look better than dots

# %%
pyplot.plot(x[2000:4000],y[2000:4000]) #plotting the next 2000 data points
pyplot.xlabel("time in s")
pyplot.ylabel("absorption")
pyplot.title("Pulse wave")

# %%
Make the plotting shorter:

# %%
# This creates the plot but shows nothing
plt.plot(x, y)
# Script ends, plot vanishes

# This actually shows the plot
plt.plot(x, y)
plt.show()  # Opens interactive window

# %%
import matplotlib.pyplot as plt 

plt.plot(x[:4000], y[:4000])
plt.xlabel("time in s")
plt.ylabel("absorption")
plt.title("Pulse wave")

plt.xlim(25, 35)  # or pyplot.xlim(25, 35)
plt.show()

# %%
plt.plot(x[:6000], y[:6000])
plt.xlabel("time in s")
plt.ylabel("absorption")
plt.title("Pulse wave")
plt.xlim(25, 40)

# %%
