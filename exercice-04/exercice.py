ventes =[
{"produit": "café", "prix": 2.5, "quantité": 12},
{"produit": "thé", "prix": 2.0, "quantité": 80},
{"produit": "jus", "prix": 3.5, "quantité": 45},
]

totaux = []

for vente in ventes:
    totaux.append({
        "produit": vente["produit"],
        "total": vente["prix"] * vente["quantité"]
    })

print(totaux)
print(sum([total["total"] for total in totaux]))

print(max([total["total"] for total in totaux]))
