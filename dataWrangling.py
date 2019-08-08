import pandas as pd


# https://opendata.dc.gov/datasets/mosquito-trap-sites
# https://zenodo.org/search?page=1&size=20&q=Manatee%20County%20Mosquito%20Control%20District
PATH = "/Users/sanchez.hmsc/Documents/GitHub/ESRi/"
FILENAME = "Mosquito_Trap_Sites.csv"

# Load and downcast
data = pd.read_csv('data/'+ FILENAME)

mem = data.memory_usage( deep=True)
cols = list(data.columns)
shp = data.shape

mem

summaryStr = '''
    Memory: {}
    Shape: {}
'''

print(summaryStr.format(mem, shp))


cats = {}
for i in cols:
    cats.update({i: set(data[i])})
    print("{}:{}".format(i, set(data[i])))
