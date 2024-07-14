lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
def bolish_listi(son, lst):
    natija = [lst[i:i + son] for i in range(0, len(lst), son)]
    return natija
oraliq = 3
korsatish = bolish_listi(oraliq, lst)
print(korsatish)
oraliq = 7
korsatish = bolish_listi(oraliq, lst)
print(korsatish)
