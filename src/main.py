import pandas as pd
import os
from fungsi import printSeries
from linearSearch import LinearSearch
from insertionSort import InsertionSort

DIR=os.path.dirname(__file__) # Path absolut

#============DATAFRAME SETUP==============
df = pd.read_csv(DIR+'/./data/input/dataset_superstore_simple.csv') # Read lokasi file csv secara relative

def sortBy(dataframe,kolom,urutan='naik',simpan=False):
  result=dataframe.copy()
  sortedList=InsertionSort(result[kolom].tolist(),kolom,urutan)

  # Reindexing...
  result['g'] = result.groupby(kolom).cumcount()
  df2 = pd.DataFrame({kolom: sortedList})
  df2['g'] = df2.groupby(kolom).cumcount()
  result=result.set_index([kolom, 'g']).reindex(df2.set_index([kolom,'g']).index).reset_index().drop('g',axis=1).reindex(columns=result.columns.tolist())

  if simpan:
    result.to_csv(DIR+'/./data/output/sorted/'+kolom+'-'+urutan+'.csv',index=False)
  return result

def searchBy(dataframe,kolom,cari):
  return LinearSearch(dataframe[kolom],cari) # Mengembalikan indeks
#=========================================

sortedDF=sortBy(df,'order_date',urutan='turun',simpan=True)
print(sortedDF)
atIndex=searchBy(df,'sales',258.576)
print(atIndex)