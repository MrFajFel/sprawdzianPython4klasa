class Stack:
    def __init__(self):
        self.tab = []



    def isEmpty(self):
        if self.tab[0] is None:
            raise Exception("lista jest pusta")


    def add(self,imie,nazwisko):
        slownik = {"imie:":imie,"nazwisko":nazwisko}
        self.tab.append(slownik)


    def pop(self):
        if self.isEmpty():
            return False
        self.tab.pop(0)

    def peek(self):
        print(self.tab)