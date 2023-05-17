def stalemate(pola):
    flat = sum(pola, [])
    licz = flat.count(-1)
    if licz >0:
        return False
    elif licz == 0:
        return True