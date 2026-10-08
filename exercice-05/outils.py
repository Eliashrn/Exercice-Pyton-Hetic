def moyenne(notes):
    valides = []
    for n in notes:
        if isinstance(n, (int, float)):
            valides.append(n)

    if len(valides) == 0:
        return 0

    return sum(valides) / len(valides)

def convertir_texte(texte):
    try:
        return float(texte)
    except ValueError:
        print(f"Erreur : '{texte}' n'est pas un nombre valide")
        return None


def mention(note):
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "Passable"
    elif note < 14:
        return "Assez bien"
    elif note < 16:
        return "Bien"
    else:
        return "Très bien"