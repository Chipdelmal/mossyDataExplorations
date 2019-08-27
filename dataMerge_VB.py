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

# ############################################################################
# Setup paths
# ############################################################################
PATH = "/Volumes/marshallShare/FieldData/"
FILEPATHS = glob.glob(PATH + "VectorBase*")[0::1]
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
MAX_REQUESTS = 500
dictsList = []
for i in range(MAX_REQUESTS):
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
daw.to_csv(path_or_buf=(PATH + "Clean/VectorBase_mergedDAW.csv"))
