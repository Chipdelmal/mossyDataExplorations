#!/usr/bin/python
# -*- coding: utf-8 -*-

# ############################################################################
# Data Sources:
#
# ############################################################################
import pandas as pd

def listColumnsNumbers(data):
    return ["{}. {}".format(i, col) for (i, col) in enumerate(list(data.columns))]

# ############################################################################
# Set paths and filenames
# ############################################################################
FILE = 'BAS_20190611_Reporte_colectas_insectario_ADB_V02.xlsx'
PATH = '/Volumes/marshallShare/Ecuador/'
FILEPATH = PATH + FILE

# ############################################################################
# Load raw dataset
#   0. 3a.detalle_inmaduros
#   1. 3b.conteo_inicial_inm_rural
#   2. 3b.detalle_inmaduros_rural
#   3. 4.conteo_inicial_adultos
#   4. 4.registro_adultos_detalle
# ############################################################################

# ############################################################################
# Cleaning: 3a.detalle_inmaduros
dataImm = pd.read_excel(
    FILEPATH,
    sheet_name='3a.detalle_inmaduros',
    parse_dates=[0, 13]
)
dataImm.head()
set(dataImm['Circuito'])
listColumnsNumbers(dataImm)


# ############################################################################
# Cleaning: 3b.conteo_inicial_inm_rural
dataImmIR = pd.read_excel(
    FILEPATH,
    sheet_name='3b.conteo_inicial_inm_rural',
)
listColumnsNumbers(dataImmIR)


# ############################################################################
# Cleaning: 3b.detalle_inmaduros_rural
dataImmFR = pd.read_excel(
    FILEPATH,
    sheet_name='3b.detalle_inmaduros_rural',
)
listColumnsNumbers(dataImmFR)


# ############################################################################
# Cleaning: 4.conteo_inicial_adultos
dataAdI = pd.read_excel(
    FILEPATH,
    sheet_name='4.conteo_inicial_adultos',
)
listColumnsNumbers(dataAdI)


# ############################################################################
# Cleaning: 4.registro_adultos_detalle
dataAdD = pd.read_excel(
    FILEPATH,
    sheet_name='4.registro_adultos_detalle',
)
listColumnsNumbers(dataAdD)
