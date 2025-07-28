
def suma_diapazonu(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


def dobutok_spysku(spysok):
    dob = 1
    for x in spysok:
        dob *= x
    return dob







def minimum_spysku(spysok):
    return min(spysok)




def prostie_chysla(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def kilkist_prostych(spysok):
    return sum(1 for x in spysok if prostie_chysla(x))





def vydalyty_chyslo(spysok, chyslo):
    k = spysok.count(chyslo)
    spysok = [x for x in spysok if x != chyslo]
    return k



