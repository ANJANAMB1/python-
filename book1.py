class Python(Book):
  def __init__(self, pname):
   Book__init__(self, pname)
  def details(self):
        self._price = int(input("Book Price:"))
        self._pages = int(input("Book Pages :"))

  def display(self):
        print("Publisher :", self.pname)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self._price)
        print("Pages :", self._pages)
obj = Python("DC BOOKS")
obj.bookdetails()
obj.details()
print(" ")
obj.display()
