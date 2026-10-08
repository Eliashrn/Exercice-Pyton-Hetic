from outils import convertir_texte, mention, moyenne


notes = ["12,5", "15", "abc", "9", "18,25"]

notes_converties = []

for note in notes:
    note_convertie = convertir_texte(note.replace(",", "."))
    notes_converties.append(note_convertie)
    
print(notes_converties)
print(mention(notes_converties[0]))
print(moyenne(notes_converties))