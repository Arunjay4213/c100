class Book(object):
    def __init__(self, author, age, genre, numberOfBooks=None):
        self.author = author 
        self.age = age
        self.genre = genre
        self.numberOfBooks = numberOfBooks or {}


    def getInformation(self):
        return(self.author, self.age, self.genre, self.numberOfBooks)

    def setnumberOfBooks(self,num,author,numberOfBooks):
        self.numberOfBooks[num] = numberOfBooks

    def getNumberOfBooks(self,num,author):
        return self.numberOfBooks[num]

john = Book("Arunjay",16,"Fiction",{"Arunjay's secrets":3})
jane = Book("Arunjay1",16,"Non Fiction",{"Not Arunjay's secrets":5})

print(john.getInformation())
print(jane.getInformation())


print(jane.getNumberOfBooks("Arunjay"))