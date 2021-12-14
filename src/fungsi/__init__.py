def printSeries(judul:str, data): # Mempercantik print data komposit
  print(judul.center(20,'='))
  for i,d in enumerate(data):
    print((str(i)+'. '+str(d)).ljust(20)+'|')
  print(''.center(20,'='))