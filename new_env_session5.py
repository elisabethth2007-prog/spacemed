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

# %% [markdown]
# ## Session 5 - pandas

# %% [raw]
# ---
# title: "Session 5: Pandas"
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

# %%
import pandas

# %%
station_ids = pandas.read_csv("data/Niederschlag_1981-2010_Stationsliste.txt",
                              encoding="iso-8859-1", delimiter=" *; *",
                             index_col="Stations_id", engine="python")

# %%
station_ids

# %%
station_ids.columns

# %%
station_ids.info()

# %%
station_ids.head()

# %%
station_ids.tail()

# %% [markdown]
# delete last column: (unnamed) axis=1 columns, axis=0 rows

# %%
station_ids.drop(station_ids.columns[-1],axis=1, inplace=True)

# %%
station_ids.columns

# %%
station_ids.head()

# %% [markdown]
# index location, row then column

# %%
station_ids.iloc[2,0]

# %% [markdown]
# slicing by index, upper band is not included

# %%
station_ids.iloc[:5]

# %%
station_ids.iloc[:, 1:3]

# %% [markdown]
# slicing by label, upper band is included

# %%
station_ids.loc[3:6,"Stationsname"]

# %%
station_ids.loc[:,"geogr. Breite":"geogr. Laenge"]

# %%
station_ids["Bundesland"]

# %%
station_ids.Bundesland #does the same if column name has no spaces

# %%
station_ids.groupby("Bundesland").count().sort_values("Stationsname")

# %%
mask = station_ids.Bundesland == "Bayern" #creates a mask where column bundesland is bayern

# %%
bayern = station_ids[mask] #all data where the mask is true

# %%
station_ids.Bundesland.iloc[-1] #tells us what the last entry is, as a check

# %%
bayern.iloc[17]

# %% [markdown]
# Task for this session: 

# %%
mask1 = station_ids.Bundesland == "Berlin" #creates a mask where column bundesland is berlin

# %%
berlin = station_ids[mask1] #all data where the mask is true

# %%
berlin.iloc[17]

# %%
# station_ids.loc[:,"geogr. Breite":"geogr. Laenge"]

# %% [markdown]
# Assignment: load the 30 year mean precipitation data
# data/Niederschlag 1981-2010.txt
# • only keep the columns with the monthly means

# %%
precip_ref = pandas.read_csv("data/Niederschlag_1981-2010.txt",
                             encoding="iso-8859-1", delimiter=" *; *",
                             index_col="Stations_id", engine="python")

# %%
precip_ref = precip_ref.loc[:,"Jan.":"Dez."]

# %% [markdown]
# Monthly climate data:

# %%
precip_ref.loc[399].plot.bar()

# %% [markdown]
# Assignment: load the hourly data

# %%
precip = pandas.read_csv("data/produkt_precipitation_399_akt.txt",
                             encoding="iso-8859-1", delimiter=" *; *",
                                 engine="python")

# %%
precip.head()

# %%
precip.MESS_DATUM = pandas.to_datetime(precip.MESS_DATUM, format="%Y%m%d%H")

# %%
precip['date_time'] = pandas.to_datetime(precip.MESS_DATUM, format="%Y%m%d%H") #create new column

# %%
precip_alex = precip[['date_time', "NIEDERSCHLAGSHOEHE"]]

# %%
precip_alex = precip_alex.rename(columns={"date_time":"date",
                                          "NIEDERSCHLAGSHOEHE":"precipitation"})

# %%
precip_alex = precip_alex.set_index("date")

# %%
precip_alex

# %%
monthly = precip_alex.resample("ME").sum() #ME is months end

# %%
monthly.describe() #statistics over the entire year

# %%
monthly.groupby(monthly.index.month).describe() #index is date time object, count shows 11 years

# %% [markdown]
# Monthly data from Alexanderplatz: (to compare with 30 year mean precipitation data)

# %%
monthly.plot()

# %% [markdown]
# Combining with previous plot

# %%
refs = pandas.DataFrame({"precipitation": precip_ref.loc[399].to_list()*12},
                       index=pandas.date_range("2015-01-01", "2026-12-31", freq="ME"))
                        
                        #create new pandas dataframe, single column called "precipitation", 
# convert alex-data to list and repeat 12 times

# %%
refs

# %%
monthly["climate"] = refs #create a new column and assign it to dataset, 
#possible because time remains the same; alignment of indices, ignores all extra values

# %%
monthly

# %%
monthly.plot()

# %%
monthly["anomaly"] = monthly.precipitation - monthly.climate

# %% [markdown]
# It is getting drier than before

# %%
monthly.anomaly.plot()

# %% [markdown]
# Homework Session 5: 
# I don't know why this is adding anomaly to the first plot. 

# %% [markdown]
# creating multiple plots w/ pyplot.subplot

# %%
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(10, 6))

# Top plot
monthly.plot(ax=axes[0])
axes[0].set_title("Monthly Data")

# Bottom plot
monthly.anomaly.plot(ax=axes[1])
axes[1].set_title("Anomaly")

plt.tight_layout()
plt.show()
