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
# Open data in python: (Reading a Data File)

# %%
dataFile = open("data/pulse_data.csv")

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
a=numpy.arange(10)+1

# %%
a.shape

# %%
a.dtype

# %%
a.nbytes

# %%
b=numpy.array([[1,2,3],[4,5,6]])

# %%
b.shape

# %%
b.T 

# %%
b.T @b

# %%
a.T @a

# %%
a

# %%
numpy.max(a)

# %%
numpy.argmax(a)

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
absorption = numpy.array(absorption)
time = numpy.array(time)

# %%
w=50

# %%
subset = absorption #you can choose what part of the data to analyze [:1000]

# %%
peaks = []
for i in range(len(subset)):
    start = max(i-w,0)
    end = min(i+w, len(subset))
    window = subset[start:end]
    max_pos = numpy.argmax(window) + start
    if i == max_pos:
        peaks.append(i)
print(peaks)

# %%
pyplot.plot(subset)
pyplot.plot(peaks,subset[peaks], "ro")

# %%
test = numpy.arange(20)

# %%
s = test[5:10] #showing element position 5 to 9

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
time_peaks = time[peaks]

# %%
delta_t = time_peaks[1:]- time_peaks[:-1]

# %%
hr = 60 / delta_t

# %%
pyplot.plot(hr)

# %% [markdown]
# Homework session 5: use pandas and find peaks to find the peaks for calculating the hear rate

# %%
subset = absorption[:2000]

# %%
from scipy.signal import find_peaks

peaks, _ = find_peaks(subset, height=0.5, distance=50)

# %% [markdown]
# returns two things:
# peaks → indices of the peaks, properties → a dictionary with extra info (like heights, widths, etc.)
# peaks, _ = find_peaks(signal)
# The comma , is just unpacking two return values, the _ is a throwaway variable

# %%
pyplot.plot(subset)
pyplot.plot(peaks,subset[peaks], "ro")

# %% [markdown]
# Adjusting height

# %%
peaks, _ = find_peaks(subset, height=2000, distance=50)
pyplot.plot(subset)
pyplot.plot(peaks,subset[peaks], "ro")

# %% [markdown]
# Adjusting distance

# %%
peaks, _ = find_peaks(subset, height=0.5, distance=200)
pyplot.plot(subset)
pyplot.plot(peaks,subset[peaks], "ro")
