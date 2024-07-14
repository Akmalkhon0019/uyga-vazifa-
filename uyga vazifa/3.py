ls = [1, 1, 2, 3, 4, 2, 3, 4, 2, 1, 2, 3]
def karl_gauss(lst):
    sonlar = {}
    for son in lst:
        if son in sonlar:
            sonlar[son] += 1
        else:
            sonlar[son] = 1
    return sonlar

chiqish = karl_gauss(ls)
print(chiqish)
#Karl Gaus = Matematika "Qiroli".