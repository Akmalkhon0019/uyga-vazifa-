def matem(masala):
    sonlar = masala.split()
    natija = int(sonlar[0])
    hp = None

    for son in sonlar[1:]:
        if son.isdigit():
            if hp == '*':
                natija *= int(son)
            elif hp == '+':
                natija += int(son)
            elif hp == '-':
                natija -= int(son)
        elif son in ('*', '+', '-'):
            hp = son

    return f"{masala.replace('?', '')}{natija}"

kirish = "3 * 5 + 4 * 1 + 6 = ?"
chiqish = matem(kirish)
print(chiqish)
