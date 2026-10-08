produit = "clavier"
prix_ht = 19.90
prix_ttc = prix_ht * 1.2
quantity = 3
total_ht = quantity * prix_ht
total_ttc = quantity * prix_ttc

print(f"{produit}: {total_ttc} euros ttc" )
