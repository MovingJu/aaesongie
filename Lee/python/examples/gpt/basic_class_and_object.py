class Book(object):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        print(f"{self.title} by {self.author}, published in {self.year}")

if __name__ == "__main__":
    little_prince = Book("little_prince", "Lee", 2006)
    little_prince.get_description()