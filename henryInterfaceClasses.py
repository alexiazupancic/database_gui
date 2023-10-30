class Author:

    def __init__(self, author_num, author_last, author_first):
        self.author_num = float(author_num)
        self.author_last = author_last.strip()
        self.author_first = author_first.strip()
        self.name = author_first + " " + author_last

    def __str__(self):
        return f"{self.author_first} {self.author_last}"

    def get_id(self):
        return self.author_num

    def get_author_first(self):
        return self.author_first

    def get_author_last(self):
        return self.author_last


class Book:

    def __init__(self, book_code, title, publisher_code, type, price, paperback):
        self.book_code = book_code
        self.title = title
        self.publisher_code = publisher_code
        self.type = type
        self.price = float(price)
        self.paperback = paperback

    def get_book_code(self):
        return self.book_code
    
    def get_title(self):
        return self.title

    def get_price(self):
        return self.price
    
    def get_publisher_code(self):
        return self.publisher_code

    def get_type(self):
        return self.type
    
    def get_paperback(self):
        return self.paperback


class Publisher:

    def __init__(self, publisher_code, publisher_name, city):
        self.publisher_code = publisher_code
        self.publisher_name = publisher_name
        self.city = city

    def get_publisher_code(self):
        return self.publisher_code

    def get_publisher_name(self):
        return self.publisher_name
        

class Branch:

    def __init__(self, branch_num, branch_name, branch_location, num_employees):
            self.branch_num = float(branch_num)
            self.branch_name = branch_name
            self.branch_location = branch_location
            self.num_employees = float(num_employees)

    def get_branch_num(self):
        return self.branch_num

    def get_branch_name(self):
        return self.branch_name

    def get_branch_location(self):
        return self.branch_location

    def get_num_employees(self):
        return self.num_employees


class Inventory:

    def __init__(self, book_code, branch_num, on_hand):
        self.book_code = book_code
        self.branch_num = branch_num
        self.on_hand = on_hand

    def get_book_code(self):
        return self.book_code

    def get_branch_num(self):
        return self.branch_num

    def get_on_hand(self):
        return self.on_hand     


class Wrote:

    def __init__(self, book_code, author_num):
        self.book_code = book_code
        self.author_num = author_num

    def get_book_code(self):
        return self.book_code

    def get_author_num(self):
        return self.author_num