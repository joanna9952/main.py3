#exercise 1

def count_vowels(text):
    if isinstance(text, str):
        text = text.lower()
        if not all(x.isalpha() or x.isspace() for x in text):
            return 42
    else:
        return 42

    vowels = "aeiou"
    count = 0
    for x in text:
        if x in vowels:
            count += 1
    return count


text = input('Enter your text:')
print(count_vowels(text))


#exercise 2

def hamming(text1, text2):
    if len(text1) != len (text2):
        return 0
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1
    return distance

text1 = input(str('Put in your text1:'))
text2 = input(str('Put in your text2:'))
print(hamming(text1, text2))

#exercise 3

class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__ (color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"

color = input('color = ')
fuel_type = input('fuel type = ')
doors = input ('doors = ')
passengers = input('passengers = ')

print(Car(color, fuel_type, doors))
print(Bus(color, fuel_type, passengers))

#exercise 4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"

name = input('Enter the name of the book:')
author = input('Enter the name of the author:')

print(Book(name, author))

#exercise 5

class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)
            else:
                print("Error, this is not a book object.".format(book))

    def books_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book.name)
        return author_books

    def get_books(self):
        all_books = []
        for book in self.books:
            all_books.append(book.name)
        return all_books

    def clear_shelf(self):
        self.books = []

        if not self.books:
            return []


book_shelf = BookShelf()
book1 = Book("Animal Farm", "George Orwell")
book2 = Book("Fahrenheit 451", "Ray Bradbury")
book3 = "1984 by George Orwell"

book_shelf.add_book_list([book1, book2, book3])
print(book_shelf.get_books())
print(book_shelf.books_by_author("Ray Bradbury"))
book_shelf.clear_shelf()
print(book_shelf.get_books())
print(book_shelf.books_by_author("Ray Bradbury"))