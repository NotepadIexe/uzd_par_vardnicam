# 1. Izvadīt visus datus par grāmatām, katru izvadot jaunā rindā
"""
Grāmata "<<nosaukums>>" (<<gads>>), <<lappušu skaits>> lpp
"""
# 2. Atlasīt visus grāmatu nosaukumus un ierakstīt tos failā "nosaukumi.txt"
# 3. Izvadīt visvecākās grāmatas nosaukumu
# 4.1. Izvadīt visu grāmatu lapušu skaitu
# 4.2. Izvadīt visu grāmatu vidējo aritmētisko cenu
# 5.1. Izveidot funkciju garakais_nosaukums(), kas atgriež grāmatu ar garāko nosaukumu (vārdnīcas objketu)
# 5.2. Izmantojot funkciju, uz ekrāna izvadīt grāmatas autoru un gadu
# 6. Izveiodt ievad datu kopiju, un visos ierakstos, kur autors nav norādīts, ierakstīt "Nav norādīts"
"""
arr = arr.copy()
"""
# 7. Izvadīt autorus alfabētiskā secībā, lai tie neatkārtotos
# Autoru kārtošanai uz kopētā saraksta var izmantot funkciju sort(), norādot kārtošanas funkciju
"""
sort(key = lambda elem: elem[key])
"""
# vai
"""
def fun1(elem):
    return elem[key]

sort(key=fun1)
"""

# 8. Izvadīt autoru, kuram pieder visvairāk grāmatu
"""
Autors, kuram ir visvairāk grāmatu (<<grāmatu skaits>>), - <<autors>>:
1. "<<nosaukums>>"
2. "<<nosaukums>>"
...
"""
