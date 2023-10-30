import sqlite3
from henryInterfaceClasses import Author, Book, Branch, Inventory, Publisher, Wrote

class HenryDAO:
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def getAuthorData(self):
        query = "SELECT * FROM HENRY_AUTHOR"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        authors = [] #list of author objects
        for row in rows:
            author = Author(row[0], row[1], row[2])
            authors.append(author)

        return authors


    def getBookData(self):
        query = "SELECT * FROM HENRY_BOOK"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        books = []
        for row in rows:
            book = Book(row[0], row[1], row[2], row[3], row[4], row[5])
            books.append(book)

        return books


    def getPublisherData(self):
        query = "SELECT * FROM HENRY_PUBLISHER"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        publishers = []
        for row in rows:
            publisher = Publisher(row[0], row[1])
            publishers.append(publisher)
        
        return publishers

    def getBranchData(self):
        query = "SELECT * FROM HENRY_BRANCH"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        branches = []
        for row in rows:
            branch = Branch(row[0], row[1], row[2], row[3])
            branches.append(branch)
        
        return branches

    def getInventoryData(self):
        query = "SELECT * FROM HENRY_INVENTORY"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        inventory = []
        for row in rows:
            inv = Inventory(row[0], row[1], row[2])
            inventory.append(inv)

        return inventory

    def getWroteData(self):
        query = "SELECT * FROM HENRY_WROTE"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        wrote = []
        for row in rows:
            single_piece = Wrote(row[0], row[1])
            wrote.append(single_piece)
        
        return wrote



HenryDAO(db_name = "Henry.db")