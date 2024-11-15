def afficher_chemin_en_html(chemin, temps_total):
    # Dictionnaire des couleurs des lignes RATP
    couleurs_lignes_ratp = {
        "1": "#FFCE00",  # Ligne 1
        "2": "#0064B0",  # Ligne 2
        "3": "#9F9825",  # Ligne 3
        "3b": "#98D4E2",  # Ligne 3bis - Violet
        "4": "#C04191",  # Ligne 4 - Vert
        "5": "#F28E42",  # Ligne 5 - Jaune
        "6": "#83C491",  # Ligne 6 - Bleu ciel
        "7": "#F3A4BA",  # Ligne 7 - Rouge sombre
        "7b": "#83C491",  # Ligne 7bis - Turquoise
        "8": "#CEADD2",  # Ligne 8 - Violet
        "9": "#D5C900",  # Ligne 9 - Bleu marine
        "10": "#E3B32A",  # Ligne 10 - Jaune clair
        "11": "#8D5E2A",  # Ligne 11 - Bleu foncé
        "12": "#00814F",  # Ligne 12 - Rose
        "13": "#98D4E2",  # Ligne 13 - Moutarde
        "14": "#662483",  # Ligne 14 - Fuchsia
    }

    # afficher le chemin avec les couleurs de lignes
    html_chemin = "".join(
        f'<div class="station" style="color: {couleurs_lignes_ratp.get(station["ligne"], "#000000")};">'
        f'- {station["nom"]} (<span class="ligne">Ligne {station["ligne"]}</span>)</div>'
        for station in chemin
    )

    # Créer le contenu HTML complet avec le chemin et le temps total
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chemin le plus court - Métro</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #d8d8d8;
                padding: 20px;
                -webkit-text-stroke-width: 0.5px;
                -webkit-text-stroke-color: black;
            }}
            .station {{
                font-size: 18px;
                margin: 10px 0;
            }}
            .ligne {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>Chemin le plus court</h1>
        <p>Temps total estimé: {temps_total} secondes</p>
        <div>{html_chemin}</div>
    </body>
    </html>
    """

    # Sauvegarder dans un fichier HTML
    with open("chemin.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Le chemin a été sauvegardé dans 'chemin.html'")
