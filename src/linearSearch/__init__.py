from os import path
from time import time
import datetime

def LinearSearch(series,temukan):
  temukan=str(temukan)
  # START OF LOGGING
  startTime=time()
  DIR=path.dirname(__file__) # Path absolut
  
  diIndex=None
  lenArr=len(series)
  for i,d in enumerate(series):
    waktuBerlalu=time()-startTime
    print((' Mencari | '+str(d)+' | '+str(i)+'/'+str(lenArr)+' | '+str(waktuBerlalu)).ljust(10),end='\r')
    if temukan in str(d):
      diIndex=i
      endTime=time()
      break
  print()

  # END OF LOGGING
  tanggalMulai=datetime.datetime.fromtimestamp(startTime).strftime("%Y-%m-%d %H:%M:%S")
  namaKolom=series.name
  waktuBerlalu=datetime.timedelta(seconds=endTime-startTime)
  logs=[tanggalMulai,namaKolom,temukan,diIndex,waktuBerlalu]
  logLine=''
  for l in logs: logLine+=str(l)+' '
  with open(DIR+'/../data/output/lastSearch.log','a') as f: f.write(logLine+'\n')

  return diIndex
