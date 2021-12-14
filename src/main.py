import pandas as pd
import os
from fungsi import printSeries
from linearSearch import LinearSearch

DIR=os.path.dirname(__file__) # Path absolut

df = pd.read_csv(DIR+'/./data/input/dataset_superstore_simple.csv') # Read lokasi file csv secara relative

print(df.tail(),end='\n\n')
print(LinearSearch(df['sales'],'243.16'))