import tkinter as tk 
from tkinter import ttk 

def comCallback(event):
    # get will get its value - note that this is always a string
    selIndex = event.widget.current()
    print("Index selected is: " + str(selIndex))


# Main window
root = tk.Tk()
root.title("Henry Bookstore") 
root.geometry('800x400') 



# Tab control
tabControl = ttk.Notebook(root) 
tab1 = ttk.Frame(tabControl)  # tab1 and tab2 are tab window names
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Search by Author') # Blue and Red are tab titles
tabControl.add(tab2, text ='Search by Category') 
tabControl.add(tab3, text = 'Search by Publisher')
tabControl.pack(expand = 1, fill ="both") 

# Label
lab1 = ttk.Label(tab1)
lab1.grid(column=1, row=0)
lab1['text'] = "Author Selection"

# Combobox
com1 = ttk.Combobox(tab1, width = 20, state="readonly")
com1.grid(column=1, row=2)
myList = ['cat', 'dog', 'fish']
com1['values'] = myList
com1.current(0)
com1.bind("<<ComboboxSelected>>", comCallback)

# Label
lab2 = ttk.Label(tab1)
lab2.grid(column=1, row=0)
lab2['text'] = "Book Selection"

# Combobox
com2 = ttk.Combobox(tab1, width = 20, state="readonly")
com2.grid(column=1, row=2)
myList = ['cat', 'dog', 'fish']
com2['values'] = myList
com2.current(0)
com2.bind("<<ComboboxSelected>>", comCallback)


class HenrySBA:

    def __init__(self, tab_frame):
        self.tab_frame = tab_frame

        #Author selection label
        self.auth_selection = ttk.Label(tab_frame, text = "Author Selection")
        self.auth_selection.grid(column=1, row=0)

        # Combobox for author selection
        self.combobox_author = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_author.grid(column=1, row=2)
        self.combobox_author["values"] = ["author_1", "author_2", "author_3"]
        self.combobox_author.current(0)
        self.combobox_author.bind("<<ComboboxSelected>>", self.comCallback)
        self.combobox_author.grid(column=1, row=2)

        #Book Selection Label




    def __str__(self):
        return 




root.mainloop()