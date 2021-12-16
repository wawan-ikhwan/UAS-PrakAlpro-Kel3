from tkinter import Frame,StringVar,ttk,filedialog,Scrollbar,Label,Button,Entry,OptionMenu
from pandas import DataFrame,read_csv
from os import path
from linearSearch import LinearSearch
from insertionSort import InsertionSort

DIR=path.dirname(__file__) # Path absolut

def sortBy(dataframe,kolom,urutan='naik',simpan=False):
  result=dataframe.copy()
  sortedList=InsertionSort(result[kolom].tolist(),kolom,urutan)

  # Reindexing...
  result['g'] = result.groupby(kolom).cumcount()
  df2 = DataFrame({kolom: sortedList})
  df2['g'] = df2.groupby(kolom).cumcount()
  result=result.set_index([kolom, 'g']).reindex(df2.set_index([kolom,'g']).index).reset_index().drop('g',axis=1).reindex(columns=result.columns.tolist())
  result=result.drop('g',axis=1)

  if simpan:
    result.to_csv(DIR+'/./data/output/sorted/'+kolom+'-'+urutan+'.csv',index=False)
  return result

def searchBy(dataframe,kolom,cari):
  return LinearSearch(dataframe[kolom],cari) # Mengembalikan indeks

class TableViewer(Frame):

  def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.TableMargin = Frame(self.parent,width=10)
    self.TableMargin.pack()

    self.style=ttk.Style(self.TableMargin)
    self.style.theme_use('default')
    self.style.map('Treeview')

    self.tree = ttk.Treeview(self.TableMargin, height=10, selectmode='none')
    self.scrollbarX = Scrollbar(self.TableMargin, orient='horizontal',command=self.tree.xview)
    self.scrollbarY = Scrollbar(self.TableMargin, orient='vertical',command=self.tree.yview)
    self.tree.configure(yscrollcommand=self.scrollbarY.set, xscrollcommand=self.scrollbarX.set)

    self.df=DataFrame(columns=['Kolom 1','Kolom 2','Kolom 3'])
    self.updateTable(self.df)
    
    self.scrollbarX.pack(side='bottom', fill='x')
    self.scrollbarY.pack(side='right',fill='y')
    self.tree.pack()
    
  def updateTable(self,df=None):
    if df is not None:
      self.df = df
    else: pass

    # Remove current data
    for row in self.tree.get_children():
      self.tree.delete(row)
    
    #reconfigure
    self.tree.configure(columns=self.df.columns.tolist())
    
    # Heading
    for c in self.df.columns.tolist():
      self.tree.heading(c, text=c, anchor='w',command=lambda col=c:self.updateTable(sortBy(self.df,col)))
    self.tree.column('#0', stretch='no', minwidth=0, width=0)
    for i in range(1,len(self.df.columns)):
      self.tree.column('#'+str(i), stretch='no', minwidth=0, width=130)

    # Fill Data
    self.IDs=[]
    for i,row in enumerate(self.df.itertuples(index=False)):
      self.IDs.append(self.tree.insert('','end',values=row))
class MyApp(Frame):

  def __browseButton(self,initDir=None):
    if initDir is None: initDir=self.importPath.get()
    print('Importing csv...')
    filename = filedialog.askopenfilename(filetypes=[('Comma Separated Value','*.csv')],initialdir=initDir)
    if not filename:
      print('Dibatalkan')
      return
    self.importPath.set(filename)
    self.table.updateTable(read_csv(self.importPath.get()))
    self.__updateOKolom()
    print('Import Path: ',filename)
  
  def __keyPressed(self,key):
    self.__browseButton(self.importPath.get())
    print(key,self.importPath.get())

  def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.importPath=StringVar()
    self.importPath.set('.')

    # Window Setup
    self.parent.title('UAS Prak. Alpro II Kelompok 3 ')
    self.parent.geometry('860x480')

    # Baris 1
    frame1=Frame(self)
    frame1.pack(fill='x')

    LTitle=Label(frame1,text=self.parent.title())
    LTitle.config(font=('Courier',20))
    LTitle.pack()

    # Baris 2
    frame2=Frame(self)
    frame2.pack(fill='x')

    BImport=Button(frame2,text='Import CSV',command=self.__browseButton)
    BImport.config(font=('Courier',10))
    BImport.pack(side='left',padx=5,pady=5)

    EImport = Entry(frame2,width=50,textvariable=self.importPath)
    EImport.bind('<Return>', self.__keyPressed)
    EImport.pack(fill='x',padx=5,expand=True)

    # Baris 3
    frame3=Frame(self)
    frame3.pack(fill='x')

    self.table=TableViewer(frame3)
    self.table.pack(fill='x',expand=False)

    # Baris 4
    frame4=Frame(self)
    frame4.pack(fill='x')
    self.cari=StringVar()
    self.cari.set('')

    self.frame4_1=Frame(frame4)
    self.frame4_1.pack(side='left')
    self.opsiKolom=StringVar(self.frame4_1)
    self.__updateOKolom()


    def cariCallback():
      try:
        atIndex=searchBy(self.table.df,self.opsiKolom.get(),self.cari.get())
        selections=[]
        for i in atIndex:
          selections.append(self.table.IDs[i])
        self.table.tree.yview_moveto(atIndex[0]/len(self.table.df.index))
        self.table.tree.selection_set(selections)
      except: pass
    BCari=Button(frame4,text='Cari',command=cariCallback)
    BCari.config(font=('Courier',10))
    BCari.pack(side='left')

    ECari = Entry(frame4,textvariable=self.cari)
    ECari.pack(fill='x',expand=True)
  
  def __updateOKolom(self):
    try:
      self.OKolom.destroy()
    except: pass
    self.opsiKolom.set(self.table.df.columns[0])
    self.OKolom=OptionMenu(self.frame4_1,self.opsiKolom,*self.table.df.columns)
    self.OKolom.pack(side='left')