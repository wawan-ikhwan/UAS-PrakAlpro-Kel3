import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from os import path
from main import sortBy,searchBy
DIR=path.dirname(__file__) # Path absolut

class TableViewer(tk.Frame):
  def __init__(self, parent,df, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.df=df
    self.dfCol=self.df.columns.tolist()

    self.TableMargin = tk.Frame(self.parent, width=320, height=320)
    self.TableMargin.pack(side='top',expand=False)
    self.scrollbarX = tk.Scrollbar(self.TableMargin, orient='horizontal')
    self.scrollbarY = tk.Scrollbar(self.TableMargin, orient='vertical')
    self.tree = ttk.Treeview(self.TableMargin, columns=self.dfCol, height=100, selectmode='browse', yscrollcommand=self.scrollbarY.set, xscrollcommand=self.scrollbarX.set)
    self.scrollbarY.config(command=self.tree.yview)
    self.scrollbarY.pack(side='right', fill='y')
    self.scrollbarX.config(command=self.tree.xview)
    self.scrollbarX.pack(side='bottom', fill='x')

    for c in self.dfCol:
      self.tree.heading(c, text=c, anchor='w')

    self.tree.column('#0', stretch='no', minwidth=0, width=0)

    for i in range(1,len(self.dfCol)):
      self.tree.column('#'+str(i), stretch='no', minwidth=0, width=100)
    
    self.tree.pack(expand=False)

    for row in self.df.itertuples(index=False):
      self.tree.insert('', 0, values=list(row))

  def hancurkan(self):
    print('destroyed')
    self.scrollbarX.destroy()
    self.scrollbarY.destroy()
    self.TableMargin.destroy()
    self.tree.destroy()
    self.destroy()

class MyApp(tk.Frame):

  def __browseButton(self,initDir=None):
    if initDir is None: initDir=self.importPath.get()
    filename = filedialog.askopenfilename(filetypes=[('Comma Separated Value','*.csv')],initialdir=initDir)
    if not filename:
      print('Dibatalkan')
      return
    self.importPath.set(filename)
    self.__updateTable(pd.read_csv(self.importPath.get()))
    print(filename)
  
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
    self.parent.geometry('640x480')

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
    self.frame3=TableViewer(self,pd.DataFrame(columns=['Kolom1','Kolom2','Kolom3']))
    self.frame3.pack(fill='x',expand=False)

    # Baris 4
    frame4=tk.Frame(self)
    frame4.pack(fill='x')
    BCari=tk.Button(frame4,text='Cari',command=lambda: self.frame3.hancurkan())
    BCari.config(font=('Courier',10))
    BCari.pack(side='left',padx=5,pady=5)

    ECari = tk.Entry(frame4,width=50,textvariable='foo')
    ECari.pack(fill='x',padx=5,expand=True)
  
  def __updateTable(self,df):
    self.frame3.hancurkan()
    self.frame3=TableViewer(self.parent,df)
    self.frame3.pack(fill='x')

if __name__ == "__main__":
  root = tk.Tk()
  MyApp(root).pack(expand=True)
  root.mainloop()