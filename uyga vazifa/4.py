mashinalar = [
    {"model": "RDX", "yil": 2009},
    {"model": "LS", "yil": 2000},
    {"model": "GLK-Class", "yil": 2010},
    {"model": "Express 1500", "yil": 2005},
    {"model": "LR2", "yil": 2008},
    {"model": "XF", "yil": 2012},
    {"model": "MR2", "yil": 2005},
    {"model": "Malibu", "yil": 2007},
    {"model": "M-Class", "yil": 2010},
    {"model": "Routan", "yil": 2011}
]
def sortirovka(mashinalar):
    return sorted(mashinalar, key=lambda x: x["yil"])

chiqish = sortirovka(mashinalar)
for m in chiqish:
    print(m)