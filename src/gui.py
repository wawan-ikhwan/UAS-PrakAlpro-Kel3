import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import filedialog
import pandas as pd
from os import path
from main import sortBy,searchBy
DIR=path.dirname(__file__) # Path absolut

class TableViewer(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.lastXPos=(0.0,1.0)

    self.TableMargin = tk.Frame(self.parent)
    self.TableMargin.pack()

    self.style=ttk.Style(self.TableMargin)
    self.style.theme_use('default')
    self.style.map('Treeview')

    self.df=pd.DataFrame(columns=['Kolom 1','Kolom 2','Kolom 3'])
    self.updateTable(self.df)


  def destroyTable(self):
    try:
      self.scrollbarX.destroy()
      self.scrollbarY.destroy()
      self.tree.destroy()
    except: pass
    
  def updateTable(self,df=None):
    self.destroyTable()
    if df is not None:
      self.df = df
    self.tree = ttk.Treeview(self.TableMargin, columns=self.df.columns.tolist(), height=10, selectmode='none')
    self.scrollbarX = tk.Scrollbar(self.TableMargin, orient='horizontal',command=self.tree.xview)
    self.scrollbarY = tk.Scrollbar(self.TableMargin, orient='vertical',command=self.tree.yview)

    self.tree.configure(yscrollcommand=self.scrollbarY.set, xscrollcommand=self.scrollbarX.set)
    
    # Heading
    for c in self.df.columns.tolist():
      self.tree.heading(c, text=c, anchor='w',command=lambda col=c: 
        self.updateTable(sortBy(self.df,col))
      )
    self.tree.column('#0', stretch='no', minwidth=0, width=0)
    for i in range(1,len(self.df.columns)):
      self.tree.column('#'+str(i), stretch='no', minwidth=0, width=130)

    self.scrollbarX.pack(side='bottom', fill='x')
    self.scrollbarY.pack(side='right',fill='y')
    self.tree.pack()

    # Fill Data
    self.IDs=[]
    for i,row in enumerate(self.df.itertuples(index=False)):
      self.IDs.append(self.tree.insert('','end',values=row))
class MyApp(tk.Frame):

  def __browseButton(self,initDir=None):
    if initDir is None: initDir=self.importPath.get()
    print('Importing csv...')
    filename = filedialog.askopenfilename(filetypes=[('Comma Separated Value','*.csv')],initialdir=initDir)
    if not filename:
      print(self.table.lastXPos)
      print('Dibatalkan')
      return
    self.importPath.set(filename)
    self.table.updateTable(pd.read_csv(self.importPath.get()))
    self.__updateOKolom()
    print('Import Path: ',filename)
  
  def __keyPressed(self,key):
    self.__browseButton(self.importPath.get())
    print(key,self.importPath.get())

  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.importPath=tk.StringVar()
    self.importPath.set('C:\\UAS-PrakAlpro-Kel3')

    # Window Setup
    self.parent.title('UAS Prak. Alpro II Kelompok 3 ')
    self.parent.geometry('860x480')

    # Baris 1
    frame1=tk.Frame(self)
    frame1.pack(fill='x')

    LTitle=tk.Label(frame1,text=self.parent.title())
    LTitle.config(font=('Courier',20))
    LTitle.pack()

    # Baris 2
    frame2=tk.Frame(self)
    frame2.pack(fill='x')

    BImport=tk.Button(frame2,text='Import CSV',command=self.__browseButton)
    BImport.config(font=('Courier',10))
    BImport.pack(side='left',padx=5,pady=5)

    EImport = tk.Entry(frame2,width=50,textvariable=self.importPath)
    EImport.bind('<Return>', self.__keyPressed)
    EImport.pack(fill='x',padx=5,expand=True)

    # Baris 3
    frame3=tk.Frame(self)
    frame3.pack(fill='x')

    self.table=TableViewer(frame3)
    self.table.pack(fill='x',expand=False)

    # Baris 4
    frame4=tk.Frame(self)
    frame4.pack(fill='x')
    self.cari=StringVar()
    self.cari.set('')

    self.frame4_1=tk.Frame(frame4)
    self.frame4_1.pack(side='left')
    self.opsiKolom=tk.StringVar(self.frame4_1)
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
    BCari=tk.Button(frame4,text='Cari',command=cariCallback)
    BCari.config(font=('Courier',10))
    BCari.pack(side='left')

    ECari = tk.Entry(frame4,textvariable=self.cari)
    ECari.pack(fill='x',expand=True)
  
  def __updateOKolom(self):
    try:
      self.OKolom.destroy()
    except: pass
    self.opsiKolom.set(self.table.df.columns[0])
    self.OKolom=tk.OptionMenu(self.frame4_1,self.opsiKolom,*self.table.df.columns)
    self.OKolom.pack(side='left')

if __name__ == "__main__":
  root = tk.Tk()
  MyApp(root).pack(expand=True)
  root.mainloop()