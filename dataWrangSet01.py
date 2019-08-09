#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://opendata.dc.gov/datasets/mosquito-trap-sites
# ############################################################################

import pandas as pd

# ############################################################################
# Set paths and filenames
# ############################################################################
PATH = "/Users/sanchez.hmsc/Documents/GitHub/ESRi/"
FILENAME = "Mosquito_Trap_Sites.csv"

# ############################################################################
# Load raw dataset
# ############################################################################
data = pd.read_csv('data/' + FILENAME, parse_dates=["TRAPCOLLECT"])

# ############################################################################
# Do some basic exploration on types and entries
# ############################################################################
mem = data.memory_usage(deep=True)
cols = list(data.columns)
shp = data.shape
print(cols)

catsOfInterest = [
    "OBJECTID", "TRAPTYPE", "ATTRACTANTSUSED",
    "LATITUDE", "LONGITUDE",
    "SETTIMEOFDAY", "TRAPCOLLECT", "COLLECTTIMEOFDAY",
    "GENUS", "SPECIES",
    "FEMALESCOLLECTED", "MALESCOLLECTED"
]
data[catsOfInterest]

# ############################################################################
# Explore trapped mosquitos
# ############################################################################
groupLabel = "TRAPTYPE"
varsLabels = ["FEMALESCOLLECTED", "MALESCOLLECTED"]
trapsNumber = data.groupby(groupLabel).count()[varsLabels]
byTrap = data.groupby(groupLabel).sum()
byTrap[labels] / trapsNumber

groupLabel = "ATTRACTANTSUSED"
trapsNumber = data.groupby(groupLabel).count()[labels]
byTrap = data.groupby(groupLabel).sum()
byTrap[labels] / trapsNumber


# ############################################################################
# Print some stats
# ############################################################################
summaryStr = 'Memory: {} \nShape: {}'
print(summaryStr.format(mem, shp))


cats = {}
for i in cols:
    cats.update({i: set(data[i])})
    print("{}:{}".format(i, set(data[i])))
