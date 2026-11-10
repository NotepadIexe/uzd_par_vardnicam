from uzd1.d import dati
# 1. Izvadīt visus datus par grāmatām, katru izvadot jaunā rindā
for x in dati:
	print(x["name"],x["pages"],x["year_published"])

# 2. Atlasīt visus grāmatu nosaukumus un ierakstīt tos failā "nosaukumi.txt"
file = open("nosaukumi.txt", "a", encoding="utf-8")
for x in dati:
    file.write(x["name"] + f"\n")
# 3. Izvadīt visvecākās grāmatas nosaukumu
old = 2011
for x in dati:
    if old > int(x["year_published"]):
         old = int(x["year_published"])
for x in dati:
    if int(x["year_published"]) == old:
        print(x["name"])
# 4.1. Izvadīt visu grāmatu lapušu skaitu
sum = 0
for x in dati:
    sum += int(x["pages"])
print(sum)
# 4.2. Izvadīt visu grāmatu vidējo aritmētisko cenu
vid = 0
sum2 = 0
z = 0
for x in dati:
    z += 1
for x in dati:
    sum2 += int(x["price"])
print(sum2/z)
# 5.1. Izveidot funkciju garakais_nosaukums(), kas atgriež grāmatu ar garāko nosaukumu (vārdnīcas objketu)
def garakais_nosaukums(dati):
    o = " "
    for x in dati:
        if len(x["name"]) > len(o):
            o = x["name"]
    print(o)
garakais_nosaukums(dati)
# 5.2. Izmantojot funkciju, uz ekrāna izvadīt grāmatas autoru un gadu
def gaug(dati):
    for x in dati:
        print(x["name"],x["author"])
gaug(dati)
# 6. Izveiodt ievad datu kopiju, un visos ierakstos, kur autors nav norādīts, ierakstīt "Nav norādīts"
dati2 = dati.copy()
for x in dati2:
    if x["author"] == "":
        print(x["name"],"Autors nav noradits")
# 7. Izvadīt autorus alfabētiskā secībā, lai tie neatkārtotos
sar=[]
for x in dati:
    if x not in sar:
    	sar.append(x["author"])
print(sar)
# 8. Izvadīt autoru, kuram pieder visvairāk grāmatu
i = 0
g: str = None
for x in dati:
    o = 0
    for y in dati:
        if x["author"] == y["author"]:
            o += 1
    if o > i:
        g = x["author"]
    else:
        continue
    i = o
print(g)