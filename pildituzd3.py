from dati import skirosana
from collections import Counter
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot baterijas un akumulatorus.
i = 0
for x in skirosana["result"]["records"]:
    if x["8 : Baterijas un akumulatori"] == "x" or x["8 : Baterijas un akumulatori"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
        else:
            "ierakstu nav"
        i += 1
print(i)
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot nolietotās riepas.
i = 0
for x in skirosana["result"]["records"]:
    if x["10 : Nolietotās riepas"] == "x" or x["10 : Nolietotās riepas"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
        else:
            "ierakstu nav"
        i += 1
print(i)
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot metālu.
i = 0
for x in skirosana["result"]["records"]:
    if x["3 : Metāls"] == "x" or x["3 : Metāls"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
        else:
            "ierakstu nav"
        i += 1
print(i)
# Izvadīt novadu, kurā atrodas visvairāk atkritumu skirosanas punktu
#1. Leanaaaaaaaaaaaks
from time import perf_counter
t1 = perf_counter()
i = 0
g: str = None
ipreks = ""
for x in skirosana["result"]["records"]:
    o = 0
    if ipreks == x["pilsetanovads"]:
        continue
    ipreks = x["pilsetanovads"]
    for y in skirosana["result"]["records"]:
        if x["pilsetanovads"] == y["pilsetanovads"]:
            o += 1
    if o > i:
        g = x["pilsetanovads"]
    else:
        continue
    i = o
print(g, i)
#2. Daudz atraaaaaaaaks
t2 = perf_counter()
i = 0
o = []
for x in skirosana["result"]["records"]:
    o.append(x["pilsetanovads"])
o = Counter(o).most_common(1)[0]
print(o)
t3 = perf_counter()
print(t2-t1)
print(t3-t2)
# Izvadīt visu novadu skaitu, kuros atrodas vismaz viena katra veida šķirošanas iespēja
i = 0
for x in skirosana["result"]["records"]:
    if 'x' in skirosana["result"]["records"][1].values():
        i += 1
print(i)