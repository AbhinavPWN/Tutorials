class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.prices = price

    def __str__(self) -> str:  # returns always strings
        return f"{self.title} is written by  {self.author} "

    def __len__(self):
        return self.prices


obj1 = Book('The alchemist', 'Paulo coelho', 500)
print(obj1)
print(len(obj1))
