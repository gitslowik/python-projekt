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