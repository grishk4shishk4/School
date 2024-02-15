a = [int(i) for i in open('C:/Users/Gregoriy Mukhin/Downloads/27-B_12257.txt')]
pref_ost = []
min_pref = len(a)
c = 0

for i in a:
    c += i
    pref_ost.append(c)

pref_ost = list(map(lambda x: x % 113, pref_ost))

for i in range(113):
    min_pref = min(pref_ost.index(i) + list(reversed(pref_ost)).index(i), min_pref)

print(len(a) - (min_pref + 1))