from os import path
from time import time
import datetime

def LinearSearch(series,temukan):
  temukan=str(temukan)
  # START OF LOGGING
  startTime=time()
  DIR=path.dirname(__file__) # Path absolut
  
  diIndex=[]
  lenArr=len(series)
  maxIndex=lenArr-1
  for i,d in enumerate(series):
    waktuBerlalu=time()-startTime
    print((' Mencari '+temukan+' | '+str(i)+'/'+str(maxIndex)+' | '+str(waktuBerlalu)).ljust(55),end='\r')
    if temukan in str(d):
      diIndex.append(i)
  endTime=time()
  print()

  # END OF LOGGING
  tanggalMulai=datetime.datetime.fromtimestamp(startTime).strftime("%Y-%m-%d %H:%M:%S")
  namaKolom=series.name
  waktuBerlalu=datetime.timedelta(seconds=endTime-startTime)
  logs=[tanggalMulai,namaKolom,temukan,diIndex,waktuBerlalu]
  logLine=''
  for l in logs: logLine+=str(l)+' '
  try: open(DIR+'/../data/output/lastSearch.log','a').write(logLine+'\n')
  except: open('./lastSearch.log','a').write(logLine+'\n')

  return diIndex
