#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://zenodo.org/search?page=1&size=20&q=Manatee%20County%20Mosquito%20Control%20District
# ############################################################################
import pandas as pd

# ############################################################################
# Set paths and filenames
# ############################################################################
year = 2016
(PATH, FILENAME) = (
    "/Users/sanchez.hmsc/Documents/GitHub/mozzieDataExplorations/",
    "VectorBase-" +
        str(year) +
        "-Manatee_County_Mosquito_Control_District_Florida_USA.csv"
)

# ############################################################################
# Load raw dataset
# ############################################################################
data = pd.read_csv('data/' + FILENAME)
list(data.columns)

# ############################################################################
# Do some basic exploration on types and entries
# ############################################################################
mem = data.memory_usage(deep=True)
cols = list(data.columns)
shp = data.shape
print(cols)


# ############################################################################
# Print variables sets
# ############################################################################
cats = {}
for i in cols:
    cats.update({i: set(data[i])})
    print("{}:{}".format(i, set(data[i])))
