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
# esc-r makes a raw cell, just plain text (markdown and code are executed)

# %% [raw]
# ---
# title: "Session 4: Reproducible Documents"
# author: Elisabeth Thamm
# format:
#   html:
#     code-fold: true
#   pdf:
#     echo: false
#     pdf-engine: pdflatex
#     toc: true
#     number-depth: 2
#     number-sections: true
#     papersize: a4
#     documentclass: article
# jupyter: python3
# ---

# %% [raw]
# Raw vs Markdown Overview:
#
# # is a heading, $ equation $$ equation on seperate line
#
# # Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# _constant mass flow rate_ $R$ meassured in kg/s
# and _exhaust velocity relative to the rocket_
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$ {#eq-rocket-acc}
# Integrating both sides of @eq-rocket-acc from 0
# to $T$ we get

# %% [markdown]
# # Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# _constant mass flow rate_ $R$ meassured in kg/s
# and _exhaust velocity relative to the rocket_
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$ {#eq-rocket-acc}
# Integrating both sides of @eq-rocket-acc from 0
# to $T$ we get

# %% [markdown]
# #Open data in python: (Reading a Data File)

# %%
#dataFile = open("../data/pulse_data.csv") # open file in same directory

# %% [markdown]
# create an empty list:

# %%
#time = []
#absorption = []

# %% [markdown]
# 20.04.2026 Opening the data with a function: 1)move the data loader to a function called read_pulse

# %% [markdown]
# Input: name of the file, Output: time and absorption

# %%
def read_pulse(fname):
    dataFile = open(fname)
    time = []
    absorption = []

    dataFile.readline() #discarding first line (header)
    for line in dataFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption


# %%
time, absorption = read_pulse("../data/pulse_data.csv") #returns 2 variables (tuple)
#(automatically assigns the poition of the elements; you assign 2 things and it returns 2 things)

# %% [markdown]
# Numpy is on the Charité server, for calculating things like matlab; matplotlib is another library, pyplot is a collection within

# %%
import numpy
from matplotlib import pyplot

# %% [markdown]
# Homework session 3 removed

# %%
x=time
y=absorption

# %%
#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"
pyplot.plot(time,absorption)
pyplot.xlabel("time [s]")

# %%
a=numpy.arange(10)+1 # creating an array, arange returns evenly spaced values in a given interval, 
# +1 starting with 1 instead of 0

# %%
a.shape # returns a tuple, gives length of array dimension

# %%
a.dtype #data type object (64bit (standard size) integer)

# %%
a.nbytes # how many bytes the array occupies

# %%
b=numpy.array([[1,2,3],[4,5,6]])

# %%
b.shape # That NumPy array is a 2×3 matrix (2 rows, 3 columns). Written out, it looks like this:
#[[1, 2, 3],
# [4, 5, 6]]

# %%
b.T #transpose (rows to columns)

# %%
b.T @b #matrix multiplied

# %%
a.T @a

# %%
a

# %%
numpy.max(a) #highest value

# %%
numpy.argmax(a) #position of hightest value

# %% [raw]
# for i in range (data)
#   #i becomes each point
#   start = max(i-w,0) #its an either or
#   end = i+w
#     min(i+w,len(data))
#
#
# window-size w

# %%
absorption = numpy.array(absorption) #turn list to array
time = numpy.array(time)

# %%
w=50

# %%
subset = absorption #you can choose what part of the data to analyze [:1000]

# %%
peaks = [] #empty list to store indices of peaks
for i in range(len(subset)): #Go through each position i in your array subset.
    start = max(i-w,0) # max chooses the higher value of both for boundaries of window
    end = min(i+w, len(subset)) # min chooses the lower value of both for boundaries of window
    window = subset[start:end] #sliding window
    max_pos = numpy.argmax(window) + start #position of hightest value in window, +start: index is relative to the window (starts at 0), you add start to convert it back to the original array index.
    if i == max_pos: #If the current index i is exactly where the maximum occurs in its window…then i is a local maximum within that window.
        peaks.append(i)
print(peaks)

# %%
pyplot.plot(subset)
pyplot.plot(peaks,subset[peaks], "ro") #x=location of peak, y is height of peaks

# %%
test = numpy.arange(20)

# %%
s = test[5:10] #showing element position 5 to 9, lower bound inclusive, upper bound exclusive
# startindex is the position (value) you give him

# %%
s

# %%
test

# %% [raw]
# Homework: how to compute the HR
# HR= 60/ delta Tpeaks
# tp = time[peaks]
# tp[1:]-tp[:-1]

# %%
time_peaks = time[peaks] #x=time, see above

# %%
delta_t = time_peaks[1:]- time_peaks[:-1] 
#Everything from index 1 onward (drops the first element)-
#Everything up to (but not including) the last element (e.g. X2-X1, X3-X2,...)

# %%
hr = 60 / delta_t #bpm

# %%
pyplot.plot(hr)

# %%
