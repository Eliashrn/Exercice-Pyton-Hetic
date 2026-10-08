temperature = 15
annee = 2015

if temperature < 0:
    print("gel")
elif temperature < 15:
    print("froid")
else:
    print("chaud")


if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
    print("bissextile")
elif annee % 4 == 0 and annee % 100 == 0:
         print("bissextile")
else:
    print("non bissextile")