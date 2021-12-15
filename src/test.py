import tkinter as tk
from tkinter import ttk
import pandas as pd

class TableViewer(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

    self.df=pd.DataFrame(columns=['Kolom 1','Kolom 2','Kolom 3'])

    self.TableMargin = tk.Frame(self.parent)
    self.TableMargin.pack()

    self.updateTable()

  def destroyTable(self):
    try:
      self.scrollbarX.destroy()
      self.scrollbarY.destroy()
      self.tree.destroy()
    except: pass
    
  def updateTable(self):
    self.destroyTable()
    self.scrollbarX = tk.Scrollbar(self.TableMargin, orient='horizontal')
    self.scrollbarY = tk.Scrollbar(self.TableMargin, orient='vertical')
    self.tree = ttk.Treeview(self.TableMargin, columns=self.df.columns.tolist(), height=5, selectmode='extended', yscrollcommand=self.scrollbarY.set, xscrollcommand=self.scrollbarX.set)
    self.scrollbarY.config(command=self.tree.yview)
    self.scrollbarY.pack(side='right',fill='y')
    self.scrollbarX.config(command=self.tree.xview)
    self.scrollbarX.pack(side='bottom', fill='x')
    
    for c in self.df.columns.tolist():
      self.tree.heading(c, text=c, anchor='w')

    self.tree.column('#0', stretch='no', minwidth=0, width=0)

    for i in range(1,len(self.df.columns.tolist())):
      self.tree.column('#'+str(i), stretch='no', minwidth=0, width=100)
    
    self.tree.pack()

    for row in self.df.itertuples(index=False):
      self.tree.insert('', 0, values=list(row))

if __name__=='__main__':
  root = tk.Tk()
  TableViewer(root).pack(expand=True)
  root.mainloop()