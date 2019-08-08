#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://opendata.dc.gov/datasets/mosquito-trap-sites
#   https://zenodo.org/search?page=1&size=20&q=Manatee%20County%20Mosquito%20Control%20District
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
data = pd.read_csv('data/' + FILENAME)

# ############################################################################
# Do some basic exploration on types and entries
# ############################################################################

mem = data.memory_usage(deep=True)
cols = list(data.columns)
shp = data.shape
print(cols)

catsOfInterest = [
    "TRAPTYPE", "ATTRACTANTUSED",
    "TRAPCOLLECT", "SETTIMEOFDAY", "COLLECTTIMEOFDAY",
    "GENUS", "SPECIES",
     "FEMALESCOLLECTED", "MALESCOLLECTED"
]



# ############################################################################
# Catches by trap type
# ############################################################################
labels = ["FEMALESCOLLECTED", "MALESCOLLECTED"]
trapsNumber = data.groupby("TRAPTYPE").count()[labels]
byTrap = data.groupby("TRAPTYPE").sum()
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
