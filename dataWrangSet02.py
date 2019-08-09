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
PATH = "/Users/sanchez.hmsc/Documents/GitHub/mozzieDataExplorations/"
FILENAME = "VectorBase-2016-Manatee_County_Mosquito_Control_District_Florida_USA.csv"

# ############################################################################
# Load raw dataset
# ############################################################################
data = pd.read_csv('data/' + FILENAME, parse_dates=["TRAPCOLLECT"])
