from shutil import ExecError


class Queue:
    def __init__(self):
        self.kupujacy = []



    def isEmpty(self):
        if self.kupujacy[0] is None:
            raise Exception("lista jest pusta")


    def add(self,imie,nazwisko):
        slownik = {"imie":imie,"nazwisko":nazwisko}
        self.kupujacy.append(slownik)

    def remove(self):
        if self.isEmpty():
            return False
        self.kupujacy.pop()


    def show(self):
        print(self.kupujacy)


