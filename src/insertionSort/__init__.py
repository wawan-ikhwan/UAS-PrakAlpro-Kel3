from os import path
from time import time
import datetime

def InsertionSort(arr,namaKolom : str,urutan:str='naik'):
  # START OF LOGGING
  startTime=time()
  DIR=path.dirname(__file__) # Path absolut
  tanggalMulai=datetime.datetime.fromtimestamp(startTime).strftime("%Y-%m-%d %H:%M:%S")
  
  result=arr
  lenArr=len(result)
  maxIndex=lenArr-1
  for i in range(1,lenArr):
    waktuBerlalu=time()-startTime
    hold=result[i]

    # SWAPPING
    pointer=i-1
    while pointer>=0 and hold < result[pointer]:
      result[pointer+1]=result[pointer]
      pointer-=1
    result[pointer+1]=hold

    print((' Menyortir '+namaKolom+' | '+str(i)+'/'+str(maxIndex)+' | '+str(waktuBerlalu)).ljust(55),end='\r')
  print()

  # END OF LOGGING
  endTime=time()
  waktuBerlalu=datetime.timedelta(seconds=endTime-startTime)
  logs=[tanggalMulai,namaKolom,urutan,waktuBerlalu]
  logLine=''
  for l in logs: logLine+=str(l)+' '
  try: open(DIR+'/../data/output/lastSort.log','a').write(logLine+'\n')
  except: open('./lastSort.log','a').write(logLine+'\n')
  
  if urutan != 'naik': result=result[::-1]
  return result