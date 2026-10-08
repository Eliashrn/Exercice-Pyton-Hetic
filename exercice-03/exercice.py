temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

def moyenne(liste):
    return sum(liste) / len(liste)

print(round(moyenne(temperatures), 2))
print(min(temperatures), max(temperatures))

for temp in temperatures:
    if temp > 15:
        print({temp})

for i, temp in enumerate(temperatures):
    i = i + 1
    f = temp * 9/5 + 32
    print(f"jour {i}: {f:.2f}F")