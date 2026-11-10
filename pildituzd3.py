from dati import skirosana
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot baterijas un akumulatorus.
"""i = 0
z = 0
for x in skirosana["result"]["records"]:
    if x["8 : Baterijas un akumulatori"] == "x" or x["8 : Baterijas un akumulatori"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
            z += 1
        else:
            "ierakstu nav"
        i += 1
print(z) """
       
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot nolietotās riepas.
i = 0
z = 0
for x in skirosana["result"]["records"]:
    if x["10 : Nolietotās riepas"] == "x" or x["10 : Nolietotās riepas"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
            z += 1
        else:
            "ierakstu nav"
        i += 1
print(z)
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
#    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot metālu.
"""i = 0
z = 0 
for x in skirosana["result"]["records"]:
    if x["3 : Metāls"] == "x" or x["3 : Metāls"] =="X":
        if i < 10:
            print(x["_id"])
            print(x["adrese"])
            print(x["pilsetanovads"])
            z += 1
        else:
            "ierakstu nav"
        i += 1
print(z)"""