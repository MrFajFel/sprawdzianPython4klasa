from random import random, randint

from kolejka import Queue
from stos import Stack

if __name__ == '__main__':
    queue = Queue()
    stos = Stack()


    kino = [[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    # print(kino[0][0])


    print("1. dodaj do kolejki")
    print("2. zobacz kto jest w kolejce")
    uzytkownik = int(input("Wpisz liczbe, Wpisanie -1 wylaczy program: \n"))
    while uzytkownik != -1:
        if uzytkownik == 1:
            print("podaj imie:")
            imie = input("")
            print("podaj nazwisko:")
            nazwisko = input("")
            try:
                queue.add(imie,nazwisko)
                print("dodano do kolejki")
                liczba1 = randint(0,len(kino))
                liczba2 = randint(0,len(kino))

                for i in range(len(kino)):
                    if kino[liczba1][liczba2] == 1:
                        print("miejsce zajete, sprobuj ponownie pozniej")
                        queue.remove()
                        break
                    else:
                        kino[liczba1][liczba2] = 1
                        print("miejsce zarezerwowane")
                        queue.remove()
                        break
                    break
                break
            except Exception:
                print("Nie udało się dodać użytkownika do kolejki")




    # queue.add("ja","taktoja1")
    # queue.add("ja", "taktoja2")
    # queue.add("ja", "taktoja3")
    #
    # queue.remove()
    # queue.show()

