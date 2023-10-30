import tkinter as tk 
from tkinter import ttk
from henryDAO import HenryDAO


class HenrySBA:

    def __init__(self, tab_frame, dao):
        self.tab_frame = tab_frame

        #Author selection label
        self.auth_selection = ttk.Label(tab_frame, text = "Author Selection:") #creates the widget for author selection
        self.auth_selection.grid(column=10, row=10) # places the widget in a grid layout, occupyint column 10 and row 12

        # Combobox for author selection
        self.combobox_author = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_author.grid(column=10, row=12)
        #self.combobox_author["values"] = ["author_1", "author_2", "author_3"]
        self.combobox_author.bind("<<ComboboxSelected>>", self.authorSelectedCallback)

        #Book Selection Label
        self.book_selection = ttk.Label(tab_frame, text = "Book Selection:") #creates the widget for book selection
        self.book_selection.grid(column=30, row=10)

        # Combobox for book selection
        self.combobox_book = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_book.grid(column=30, row=12)
        #self.combobox_book["values"] = ["book_1", "book_2", "book_3"]
        self.combobox_book.bind("<<ComboboxSelected>>", self.bookSelectedCallback)

        #Price Label
        self.book_price_label = ttk.Label(tab_frame, text = "Price: $0.00")
        self.book_price_label.grid(column=40, row=1)

        # Tree View for Branch Name and Copies Available
        self.tree = ttk.Treeview(tab_frame, columns=('Branch Name', 'Copies Available'), show='headings')
        self.tree.heading('Branch Name', text='Branch Name')
        self.tree.heading('Copies Available', text='Copies Available')
        self.tree.grid(column=10, row=1)

        self.dao = dao
        self.populateAuthors()

        self.combobox_author.current(0) #sets the first value of the list to be displayed

    
    def populateAuthors(self):
        authors = self.dao.getAuthorData()
        author_names = [author.name for author in authors]  
        self.combobox_author["values"] = author_names

    def getBooksByAuthor(self, author_name):
        authors = self.dao.getAuthorData() #get data for all authors
        author_obj = next((author for author in authors if author.name == author_name))

        if not author_obj:
            return []

        author_num = author_obj.get_id()

        all_wrote_entries = self.dao.getWroteData()
        book_code_by_author = [wrote.get_book_code() for wrote in all_wrote_entries if wrote.get_author_num() == author_num]

        all_books = self.dao.getBookData()
        
        #filter the books to include only the ones written by the selected author
        books_by_author = [book for book in all_books if book.get_book_code() in book_code_by_author]
        return books_by_author

    def getBookPrice(self, book_title):
        all_books = self.dao.getBookData()

        for book in all_books:
            if book.get_title() == book_title:
                return book.get_price()
        
        #If no book is found...
        return 0

    def populateTreeView(self, selected_book_code):
        for item in self.tree.get_children():
            self.tree.delete(item)

        inventory_entries = [entry for entry in self.dao.getInventoryData() if entry.get_book_code() == selected_book_code]

        all_branches = self.dao.getBranchData()

        for entry in inventory_entries:
            branch_num = entry.get_branch_num()
            on_hand = entry.get_on_hand()
            branch_name = next((branch.get_branch_name() for branch in all_branches if branch.get_branch_num() == branch_num), None)

            if branch_name:
                self.tree.insert("", "end", values =(branch_name, on_hand))

    def authorSelectedCallback(self, event):
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))
        selected_author = self.combobox_author["values"][selIndex]

    # Fetch books by selected author and update combobox_book
        books = self.getBooksByAuthor(selected_author)
        book_titles = [book.title for book in books]  
        self.combobox_book["values"] = book_titles

        if book_titles: #set index only if there are books available
            self.combobox_book.current(0)
        else:
            self.combobox_book.set("No books available")


    def bookSelectedCallback(self, event):
        # Update price label
        selected_book = self.combobox_book.get()
        book_price = self.getBookPrice(selected_book)
        self.book_price_label["text"] = f"Price: ${float(book_price):.2f}"
        self.book_price_label.grid(column=40, row=1)

        selected_book_code = next((book.get_book_code() for book in self.dao.getBookData() if book.get_title() == selected_book), None)
        if selected_book_code:
            self.populateTreeView(selected_book_code)

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
        #self.combobox_category["values"] = ["category_1", "category_2", "category_3"]
        self.combobox_category.bind("<<ComboboxSelected>>", self.categorySelectedCallback)

        #Book Selection Label
        self.book_selection = ttk.Label(tab_frame, text = "Book Selection:") #creates the widget for book selection
        self.book_selection.grid(column=30, row=10)

        # Combobox for book selection
        self.combobox_book = ttk.Combobox(tab_frame, width = 20, state = "readonly")
        self.combobox_book.grid(column=30, row=12)
        #self.combobox_book["values"] = ["book_1", "book_2", "book_3"]
        self.combobox_book.bind("<<ComboboxSelected>>", self.bookSelectedCallback)

        #Price Label
        self.book_price_label = ttk.Label(tab_frame, text = "Price: $0.00")
        self.book_price_label.grid(column=40, row=1)

        # Tree View for Branch Name and Copies Available
        self.tree = ttk.Treeview(tab_frame, columns=('Branch Name', 'Copies Available'), show='headings')
        self.tree.heading('Branch Name', text='Branch Name')
        self.tree.heading('Copies Available', text='Copies Available')
        self.tree.grid(column=10, row=1)

        self.dao = dao
        self.populateCategory()

        self.combobox_category.current(0) #sets the first value of the list to be displayed
    
    def populateCategory(self):
        books = self.dao.getBookData()
        categories = list(set(book.get_type() for book in books))  #so it doesn't show duplicates
        self.combobox_category["values"] = categories

    def getBooksByCategory(self, selected_category):
        all_books = self.dao.getBookData()
        
        #filter the books to include only the ones belonging to the selected category
        books_by_category = [book for book in all_books if book.get_type() == selected_category]
        return books_by_category

    def getBookPrice(self, book_title):
        all_books = self.dao.getBookData()

        for book in all_books:
            if book.get_title() == book_title:
                return book.get_price()
        
        #If no book is found...
        return 0

    def populateTreeView(self, selected_book_code):
        for item in self.tree.get_children():
            self.tree.delete(item)

        inventory_entries = [entry for entry in self.dao.getInventoryData() if entry.get_book_code() == selected_book_code]

        all_branches = self.dao.getBranchData()

        for entry in inventory_entries:
            branch_num = entry.get_branch_num()
            on_hand = entry.get_on_hand()
            branch_name = next((branch.get_branch_name() for branch in all_branches if branch.get_branch_num() == branch_num), None)

            if branch_name:
                self.tree.insert("", "end", values =(branch_name, on_hand))

    def categorySelectedCallback(self, event):
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))
        selected_category = self.combobox_category["values"][selIndex]

        # Fetch books by selected category and update combobox_book
        books = self.getBooksByCategory(selected_category)
        book_titles = [book.title for book in books]  
        self.combobox_book["values"] = book_titles

        if book_titles: #set index only if there are books available
            self.combobox_book.current(0)
        else:
            self.combobox_book.set("No books available")


    def bookSelectedCallback(self, event):
        # Update price label
        selected_book = self.combobox_book.get()
        book_price = self.getBookPrice(selected_book)
        self.book_price_label["text"] = f"Price: ${float(book_price):.2f}"
        self.book_price_label.grid(column=40, row=1)

        selected_book_code = next((book.get_book_code() for book in self.dao.getBookData() if book.get_title() == selected_book), None)
        if selected_book_code:
            self.populateTreeView(selected_book_code)

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
tabControl.pack(expand = 1, fill = "both") 

dao = HenryDAO("Henry.db")

sba_tab = HenrySBA(tab1, dao)
sbc_tab = HenrySBC(tab2)
sbp_tab = HenrySBP(tab3)

root.mainloop()