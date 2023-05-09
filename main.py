#Podstawowy plik na którym będzie działać projekt
#Filip Słowik, Igor Curyło

def plansza(pola):
    print("  1 2 3")
    for i in range(3):
        wiersz = str(i+1) + " "
        for j in range(3):
            if pola[i][j] == -1:
                wiersz += " "
            elif pola[i][j] == 0:
                wiersz += "O"
            elif pola[i][j] == 1:
                wiersz += "X"
            if j != 2:
                wiersz += "|"
        print(wiersz)
        if i != 2:
            print("  -----")

def play_game():
    pola = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]] 
    gracz = 0
    while True:
        plansza(pola)
        print("gracz", gracz+1)
        wiersz = int(input("wprowadź wiersz z zakresu (1-3): "))
        while wiersz not in range(1,4):
            print("podaj poprawne pole")
            wiersz = int(input("wprowadź wiersz z zakresu (1-3): "))
        kol = int(input("wprowadź kolumne z zakresu (1-3): "))
        while kol not in range(1,4):
            print("podaj poprawne pole")
            kol = int(input("wprowadź kolumne z zakresu (1-3): "))
        if pola[wiersz-1][kol-1] == -1:
            pola[wiersz-1][kol-1] = gracz
            
            if gracz == 0:
                gracz = 1
            else:
                gracz = 0
        else:
            print("pole jest zajęte")

play_game()
