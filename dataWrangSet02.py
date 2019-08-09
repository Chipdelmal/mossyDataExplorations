#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://zenodo.org/search?page=1&size=20&q=Manatee%20County%20Mosquito%20Control%20District
# ############################################################################
import pandas as pd
import glob


# ############################################################################
# Setup paths and categories (cats)
# ############################################################################
PATH = "/Volumes/marshallShare/FieldData/"
FILEPATHS = glob.glob(PATH + "VectorBase*")
catsOfInterest = [
    'collection_ID', 'sample_ID', 'trap_id',
    'collection_date_start', 'collection_date_end',
    'GPS_lat', 'GPS_lon', 'location_ADM1',
    'trap_type', 'attractant',
    'trap_number', 'trap_duration',
    'species', 'identification_method',
    'developmental_stage', 'sex',
    'sample_count'
]
catsDates = ['collection_date_start', 'collection_date_end']

# ############################################################################
# Load raw dataset into data full (daf) and data of interest (doi)
# ############################################################################
dataframes = []
for file in FILEPATHS:
    dataTemp = pd.read_csv(file, parse_dates=catsDates)
    dataframes.append(dataTemp)
daf = pd.concat(dataframes, axis=0, ignore_index=True)
doi[catsOfInterest]

# ############################################################################
# Export merged
# ############################################################################
daf.to_csv(path_or_buf=(PATH + "Clean/VectorBase_mergedDAF.csv"))
doi.to_csv(path_or_buf=(PATH + "Clean/VectorBase_mergedDOI.csv"))


# ############################################################################
# Do some basic exploration on types and entries
# ############################################################################
mem = daf.memory_usage(deep=True)
cols = list(daf.columns)
shp = daf.shape
mem

 ############################################################################
# Print variables sets
# ############################################################################
cats = {}
for i in cols:
    cats.update({i: set(daf[i])})
    print("{}:{}".format(i, set(daf[i])))
