from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.tree = ttk.Treeview(self.root) #create tree
        self.sv = StringVar() #create stringvar for entry widget
        self.sv.trace("w", self.command) #callback if stringvar is updated
        self.entry = Entry(self.root, textvariable=self.sv) #create entry
        self.names = ["Jane", "Janet", "James", "Jamie"] #these are just test inputs for the tree
        self.ids = [] #creates a list to store the ids of each entry in the tree
        for i in range(len(self.names)):
            #creates an entry in the tree for each element of the list
            #then stores the id of the tree in the self.ids list
            self.ids.append(self.tree.insert("", "end", text=self.names[i]))
        self.tree.pack()
        self.entry.pack()
    def command(self, *args):
        self.selections = [] #list of ids of matching tree entries
        for i in range(len(self.names)):
            #the below if check checks if the value of the entry matches the first characters of each element
            #in the names list up to the length of the value of the entry widget
            if self.entry.get() != "" and self.entry.get() == self.names[i][:len(self.entry.get())]:
                self.selections.append(self.ids[i]) #if it matches it appends the id to the selections list
        self.tree.selection_set(self.selections) #we then select every id in the list
root = Tk()
App(root)
root.mainloop()