
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
