print('Initializing...')

from gui import MyApp,sortBy,searchBy,read_csv,DIR
from tkinter import Tk

#==============MODE CLI===================
# df = read_csv(DIR+'/./data/input/dataset_superstore_simple.csv') # Read lokasi file csv secara relative
# sortedDF=sortBy(df,'order_date',urutan='turun',simpan=True)
# print(sortedDF)
# atIndex=searchBy(df,'sales',258.576)
# print(atIndex)

#==============MODE GUI===================
if __name__ == "__main__":
  root = Tk()
  MyApp(root).pack(expand=True)
  root.mainloop()