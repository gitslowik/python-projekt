#Podstawowy plik na którym będzie działać projekt
#Filip Słowik, Igor Curyło
from random import randint
from colorama import Fore, Back, Style


def printRED(tekst):
    print(Fore.RED, tekst)
    print(Style.RESET_ALL)
def plansza(pola):
    print("  1   2   3")
    for i in range(3):
        wiersz = str(i+1) + " "
        for j in range(3):
            if pola[i][j] == -1:
                wiersz += " "
            elif pola[i][j] == 0:
                wiersz += "◯"
            elif pola[i][j] == 1:
                wiersz += "✖"
            if j != 2:
                wiersz += " │ "
        print(wiersz)
        if i != 2:
            print("  ──┼───┼──")
def check_win(pola, gracz):
    for i in range(3):
        if pola[i][0] == gracz and pola[i][1] == gracz and pola[i][2] == gracz:
            return True
        if pola[0][i] == gracz and pola[1][i] == gracz and pola[2][i] == gracz:
            return True
    if pola[0][0] == gracz and pola[1][1] == gracz and pola[2][2] == gracz:
        return True
    if pola[0][2] == gracz and pola[1][1] == gracz and pola[2][0] == gracz:
        return True
    return False

def play_game():
    pola = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]] 
    gracz = 0
    tryb = input("wybierz czy chcesz grać z komputerem (k) czy z drugim graczem (g)")
    if tryb == "g":
        while True:
            plansza(pola)
            print("gracz", gracz+1)
            wiersz = 0
            while wiersz not in range(1,4):  
                wiersz = (input("wpisz poprawny wiersz z zakresu (1-3): ")) 
                if wiersz.isnumeric():  
                    wiersz = int(wiersz) 
                    pass

            kol = 0
            while kol not in range(1,4):  
                kol = (input("wpisz poprawną kolumne z zakresu (1-3): ")) 
                if kol.isnumeric():  
                    kol = int(kol) 
                    pass

            if pola[wiersz-1][kol-1] == -1:
                pola[wiersz-1][kol-1] = gracz
                if check_win(pola, gracz):
                    if gracz == 0:
                        print(Back.GREEN)
                        plansza(pola)
                        print("gracz", gracz+1, "wygrywa!")
                        print(Style.RESET_ALL)

                    else:
                        print(Back.RED)
                        plansza(pola)
                        print("gracz", gracz+1, "wygrywa!")
                        print(Style.RESET_ALL)

                    return

                if gracz == 0:
                    gracz = 1
                else:
                    gracz = 0
            else:
                printRED("pole jest zajęte")
                
    elif tryb == "k":
        while True:
            plansza(pola)
            print("gracz", gracz+1)
            wiersz = 0
            while wiersz not in range(1,4):  
                wiersz = (input("wpisz poprawny wiersz z zakresu (1-3): ")) 
                if wiersz.isnumeric():  
                    wiersz = int(wiersz) 
                    pass
            kol = 0
            while kol not in range(1,4):  
                kol = (input("wpisz poprawną kolumne z zakresu (1-3): ")) 
                if kol.isnumeric():  
                    kol = int(kol) 
                    pass
            if pola[wiersz-1][kol-1] == -1:
                pola[wiersz-1][kol-1] = gracz
                if check_win(pola, gracz):
                    plansza(pola)
                    print("gracz", gracz+1, "wygrywa!")
                    return
            else:
                printRED("pole jest zajęte")
            flag = False
            while flag==False:
                wiersz = randint(0,2)
                kol = randint(0,2)
                if pola[wiersz][kol] == -1:
                    pola[wiersz][kol] = 1
                    flag = True
            
    else:
        print("wybierz poprawny tryb \n")
        play_game()

play_game()
