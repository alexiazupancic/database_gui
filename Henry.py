import tkinter as tk 
from tkinter import ttk 


class HenrySBA:

    def __init__(self, tab_frame):
        self.tab_frame = tab_frame

        #Author selection label
        self.auth_selection = ttk.Label(tab_frame, text = "Author Selection:") #creates the widget for author selection
        self.auth_selection.grid(column=10, row=10) # places the widget in a grid layout, occupyint column 10 and row 12

        # Combobox for author selection
        self.combobox_author = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_author.grid(column=10, row=12)
        self.combobox_author["values"] = ["author_1", "author_2", "author_3"]
        self.combobox_author.current(0) #sets the first value of the list to be displayed
        self.combobox_author.bind("<<ComboboxSelected>>", self.comCallback)

        #Book Selection Label
        self.book_selection = ttk.Label(tab_frame, text = "Book Selection:") #creates the widget for book selection
        self.book_selection.grid(column=30, row=10)

        # Combobox for book selection
        self.combobox_book = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_book.grid(column=30, row=12)
        self.combobox_book["values"] = ["book_1", "book_2", "book_3"]
        self.combobox_book.current(0) #sets the first value of the list to be displayed
        self.combobox_book.bind("<<ComboboxSelected>>", self.comCallback)

        #Price Label
        self.book_price_label = ttk.Label(tab_frame, text = "Price: $0.00")
        self.book_price_label.grid(column=40, row=1)

        # Tree View for Branch Name and Copies Available
        tree = ttk.Treeview(tab_frame, columns=('Branch Name', 'Copies Available'), show='headings')
        tree.heading('Branch Name', text='Branch Name')
        tree.heading('Copies Available', text='Copies Available')
        tree.grid(column=10, row=1)

       

    def comCallback(self, event):
    # get will get its value - note that this is always a string
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))

    def __str__(self):
        return str(self.combobox_author["values"])

class HenrySBC:

    def __init__(self, tab_frame):
        self.tab_frame = tab_frame

        #Author selection label
        self.cat_selection = ttk.Label(tab_frame, text = "Category Selection:") #creates the widget for author selection
        self.cat_selection.grid(column=10, row=10) # places the widget in a grid layout, occupyint column 10 and row 12

        # Combobox for author selection
        self.combobox_category = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_category.grid(column=10, row=12)
        self.combobox_category["values"] = ["category_1", "category_2", "category_3"]
        self.combobox_category.current(0) #sets the first value of the list to be displayed
        self.combobox_category.bind("<<ComboboxSelected>>", self.comCallback)

        #Book Selection Label
        self.book_selection = ttk.Label(tab_frame, text = "Book Selection:") #creates the widget for book selection
        self.book_selection.grid(column=30, row=10)

        # Combobox for book selection
        self.combobox_book = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_book.grid(column=30, row=12)
        self.combobox_book["values"] = ["book_1", "book_2", "book_3"]
        self.combobox_book.current(0) #sets the first value of the list to be displayed
        self.combobox_book.bind("<<ComboboxSelected>>", self.comCallback)

        #Price Label
        self.book_price_label = ttk.Label(tab_frame, text = "Price: $0.00")
        self.book_price_label.grid(column=40, row=1)

        # Tree View for Branch Name and Copies Available
        tree = ttk.Treeview(tab_frame, columns=('Branch Name', 'Copies Available'), show='headings')
        tree.heading('Branch Name', text='Branch Name')
        tree.heading('Copies Available', text='Copies Available')
        tree.grid(column=10, row=1)

       

    def comCallback(self, event):
    # get will get its value - note that this is always a string
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))

    def __str__(self):
        return str(self.combobox_author["values"])


class HenrySBP:

    def __init__(self, tab_frame):
        self.tab_frame = tab_frame

        #Author selection label
        self.pub_selection = ttk.Label(tab_frame, text = "Publisher Selection:") #creates the widget for author selection
        self.pub_selection.grid(column=10, row=10) # places the widget in a grid layout, occupyint column 10 and row 12

        # Combobox for author selection
        self.combobox_publisher = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_publisher.grid(column=10, row=12)
        self.combobox_publisher["values"] = ["publisher_1", "publisher_2", "publisher_3"]
        self.combobox_publisher.current(0) #sets the first value of the list to be displayed
        self.combobox_publisher.bind("<<ComboboxSelected>>", self.comCallback)

        #Book Selection Label
        self.book_selection = ttk.Label(tab_frame, text = "Book Selection:") #creates the widget for book selection
        self.book_selection.grid(column=30, row=10)

        # Combobox for book selection
        self.combobox_book = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_book.grid(column=30, row=12)
        self.combobox_book["values"] = ["book_1", "book_2", "book_3"]
        self.combobox_book.current(0) #sets the first value of the list to be displayed
        self.combobox_book.bind("<<ComboboxSelected>>", self.comCallback)

        #Price Label
        self.book_price_label = ttk.Label(tab_frame, text = "Price: $0.00")
        self.book_price_label.grid(column=40, row=1)

        # Tree View for Branch Name and Copies Available
        tree = ttk.Treeview(tab_frame, columns=('Branch Name', 'Copies Available'), show='headings')
        tree.heading('Branch Name', text='Branch Name')
        tree.heading('Copies Available', text='Copies Available')
        tree.grid(column=10, row=1)

    def comCallback(self, event):
    # get will get its value - note that this is always a string
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))

    def __str__(self):
        return str(self.combobox_author["values"])


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


sba_tab = HenrySBA(tab1)
sbc_tab = HenrySBC(tab2)
sbp_tab = HenrySBP(tab3)

root.mainloop()