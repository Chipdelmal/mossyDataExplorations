#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#   https://zenodo.org/communities/vb-popbio/?page=1&size=20
# ############################################################################
import aux
import glob
import datetime
import numpy as np
import pandas as pd
import apiKeys as keys
import matplotlib.pyplot as plt
%matplotlib inline

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
    "precipType", "precipProbability", "precipIntensity",
    "precipIntensityMin", "precipIntensityMax", "precipIntensityError",
    # Temperature
    "temperatureLow", "temperatureHigh",
    "temperatureMin", "temperatureMax", "humidity",
    # Wind/Clouds
    "windSpeed", "cloudCover"
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
#
# ############################################################################
probe = daf.loc[0]
(latlong, dates) = (
    (probe['GPS_lat'], probe['GPS_lon']),
    (probe['collection_date_start'], probe['collection_date_end'])
)
