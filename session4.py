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
pyplot.plot(time,absorption)
pyplot.xlabel("time [s]")

# %%
