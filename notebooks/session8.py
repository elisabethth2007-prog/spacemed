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
#     display_name: Python [conda env:.conda-spacemed]
#     language: python
#     name: conda-env-.conda-spacemed-py
# ---

# %%
from matplotlib import pyplot
import nibabel

# %%
# !pwd

# %% [markdown]
# %cd ../.. (Move up two folders from where I am right now.)

# %%
# %cd /home/elth11/SpaceMed-2026/elth11/data

# %%
anatomy = nibabel.load("fmri-data/2_Anatomy_1mm_5min.nii")

# %%
print(anatomy.header)

# %%
print(anatomy.shape)

# %%
print(anatomy.header.get_zooms())

# %%
data_anatomy = anatomy.get_fdata()

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[120, :, :].T,
    origin="lower",
    cmap="gray")

# %%
