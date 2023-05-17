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