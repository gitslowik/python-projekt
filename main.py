#w razie gdyby coś nie działało prosze otworzyć calyprojekt.py(na nim bazował cały projekt więc na pewno wszystko tam działa, ale nie jest porozdzielane na poszczególne pliki)

#Filip Słowik(gitslowik), Igor Curyło(podjeyfa)import mapa

import stalemate
import win
import mapa
from random import randint
from colorama import Fore, Back, Style

print(" ::::::::::: ::::::::::: ::::::::                              ::::::::::: :::      ::::::::                              ::::::::::: ::::::::  :::::::::: \n")
print("   :+:         :+:    :+:    :+:                                 :+:   :+: :+:   :+:    :+:                                 :+:    :+:    :+: :+:         \n")
print("  +:+         +:+    +:+                                        +:+  +:+   +:+  +:+                                        +:+    +:+    +:+ +:+          \n")
print("  +#+         +#+    +#+                 +#++:++#++:++          +#+ +#++:++#++: +#+                 +#++:++#++:++          +#+    +#+    +:+ +#++:++#      \n")
print("  +#+         +#+    +#+                                        +#+ +#+     +#+ +#+                                        +#+    +#+    +#+ +#+            \n")
print(" #+#         #+#    #+#    #+#                                 #+# #+#     #+# #+#    #+#                                 #+#    #+#    #+# #+#             \n")
print("###     ########### ########                                  ### ###     ###  ########                                  ###     ########  ##########       \n")
print("Projekt python - kółko krzyżyk\n")
print("Autorzy - Igor Curyło (podjeyfa) i Filip Słowik(gitslowik)\n")
def printRED(tekst):
    print(Fore.RED, tekst)
    print(Style.RESET_ALL)

def play_game():
    pola = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]] 
    gracz = 0
    tryb = input("wybierz czy chcesz grać z komputerem (k) czy z drugim graczem (g)")
    if tryb == "g":
        while True:
            mapa.plansza(pola)
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
                if win.check_win(pola, gracz):
                    if gracz == 0:
                        print(Back.GREEN)
                        mapa.plansza(pola)
                        print("gracz", gracz+1, "wygrywa!")
                        print(Style.RESET_ALL)

                    else:
                        print(Back.RED)
                        mapa.plansza(pola)
                        print("gracz", gracz+1, "wygrywa!")
                        print(Style.RESET_ALL)

                    return
                elif stalemate.stalemate(pola):
                    print(Back.PURPLE)
                    mapa.plansza(pola)
                    print("remis")
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
            mapa.plansza(pola)
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
                flag = False #flaga decydująca o tym czy komputer może wykonać ruch(jest ustawiana dopiero wtedy, gdy ruch jest poprawny)
                if win.check_win(pola, gracz):
                    if gracz == 0:
                        print(Back.GREEN)
                        mapa.plansza(pola)
                        print("Gracz wygrywa!")
                        print(Style.RESET_ALL)

                    else:
                        print(Back.RED)
                        mapa.plansza(pola)
                        print("Komputer wygrywa!")
                        print(Style.RESET_ALL)

                    return
                elif stalemate.stalemate(pola):
                    print(Back.PURPLE)
                    mapa.plansza(pola)
                    print("remis")
                    print(Style.RESET_ALL)
                    return
            else:
                printRED("pole jest zajęte")
            
            while flag==False:
                wiersz = randint(0,2)
                kol = randint(0,2)
                if pola[wiersz][kol] == -1:
                    pola[wiersz][kol] = 1
                    flag = True
                if win.check_win(pola, 1):
                        print(Back.RED)
                        mapa.plansza(pola)
                        print("Komputer wygrywa!")
                        print(Style.RESET_ALL)
                        return

    else:
        print("wybierz poprawny tryb \n")
        play_game()
play_game()