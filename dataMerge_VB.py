#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://zenodo.org/communities/vb-popbio/?page=1&size=20
# ############################################################################
import aux
import glob
# import datetime
# import numpy as np
import pandas as pd
import apiKeys as keys

print('yes')

# ############################################################################
# Setup paths
# ############################################################################
# path to directory mosq-data
PATH = "/Users/Mathieu/marshall_lab/mosq-data/"
# path to directory export-data
EXPORTPATH = "/Users/Mathieu/marshall_lab/export-data/"

# PATH = "/Volumes/marshallShare/FieldData/"
# WRITEPATH = PATH + "Clean/VectorBase_mergedDAW.csv"


FILEPATHS = glob.glob(PATH + "VectorBase*")
# ############################################################################
# Categories of Interest (catsOI)
# ############################################################################
catsOIVct = [
    'collection_ID', 'sample_ID', 'trap_id',
    'collection_date_start', 'collection_date_end',
    'GPS_lat', 'GPS_lon', 'location_ADM1', 'location_ADM2',
    'trap_type', 'attractant',
    'trap_number', 'trap_duration',
    'species', 'identification_method',
    'developmental_stage', 'sex',
    'sample_count'
]
catsOIVctDate = ['collection_date_start', 'collection_date_end']
catsOIWeather = [
    # Precipitation
    "precipProbability", "precipIntensity",
    # Temperature
    "temperatureLow", "temperatureHigh",
    "temperatureMin", "temperatureMax", "humidity",
    # Wind/Clouds
    "windSpeed", "cloudCover",
    # Other
    "nearest-station"
]
# ############################################################################
# Build dataframe
# ############################################################################
dataframes = []
for file in FILEPATHS:
    dataTemp = pd.read_csv(file, parse_dates=catsOIVctDate)
    dataframes.append(dataTemp)
daf = pd.concat(dataframes, axis=0, ignore_index=True, sort=False)
# ############################################################################
# Make weather requests and build a new dataframe (FIX DATE!!!!!!!)
# ############################################################################
MAX_REQUESTS = 15
MAX_REQUESTS_AT_A_TIME = 5
# num_rows = count number of rows in csv
def sum1forline(filename):
    with open(filename) as f:
        return sum(1 for line in f)
num_rows=sum1forline(EXPORTPATH + "/VectorBase_mergedDAW.csv")

# test
# num_rows=sum1forline(WRITEPATH)
print(EXPORTPATH + "/VectorBase_mergedDAW.csv")
# num_rows gives (number of rows - 1) for some reason
print('#lines = ', num_rows)

# somehow this is changing num_rows in VectorBase_mergedDAW.csv
dictsList = []
# num_rows < MAX_REQUESTS
for i in range(num_rows, num_rows + MAX_REQUESTS_AT_A_TIME):
    probeVct = daf.loc[i]
    (latlong, dates, key) = (
        (probeVct['GPS_lat'], probeVct['GPS_lon']),
        (probeVct['collection_date_start'], probeVct['collection_date_end']),
        keys.DKS_API_KEY
    )
    probeWeather = aux.requesteAndParseWeather(latlong, dates[0], key)
    filteredWeather = {cat: probeWeather[cat] for cat in catsOIWeather}
    dTemp = probeVct.to_dict()
    dTemp.update(filteredWeather)
    dictsList.append(dTemp)
daw = pd.DataFrame(dictsList)
# ############################################################################
# Export the resulting dataframe
# ############################################################################
# replaces csv
# daw.to_csv(path_or_buf=(EXPORTPATH + "/VectorBase_mergedDAW.csv"))
# appends csv to bottom of VectorBase_mergedDAW
daw.to_csv(path_or_buf=(EXPORTPATH + "/VectorBase_mergedDAW.csv"),header=False, mode = 'a')
# daw.to_csv(path_or_buf=(EXPORTPATH + "/VectorBase_testDAW.csv"),header=False, mode = 'a')


# test
# daw.to_csv(path_or_buf=(WRITEPATH))
