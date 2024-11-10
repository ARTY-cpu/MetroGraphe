def lire_metro():
    graph = {}
    edges = []
    f = open("metro.txt", "r")
    content = f.readlines()
    sommets = content[0:376]
    aretes = content[376:862]

    for line in sommets:
        parts = line.strip().split()
        num_sommet = int(parts[1])
        nom_sommet = parts[2]
        numero_ligne = int(parts[3])
        si_terminus = int(parts[4])
        branchement = int(parts[5])

        graph[num_sommet] = {
                    'nom': nom_sommet,
                    'ligne': numero_ligne,
                    'terminus': si_terminus,
                    'branchement': branchement,
                    'voisins': []  # Liste pour les voisins (stations adjacentes)
                }
    for line in aretes :
        parts = line.strip().split()
        num_sommet1 = int(parts[1])
        num_sommet2 = int(parts[2])
        temps = int(parts[3])
        
        # Ajout de l'arête dans les voisins de chaque sommet
        graph[num_sommet1]['voisins'].append((num_sommet2, temps))
        graph[num_sommet2]['voisins'].append((num_sommet1, temps))
        
        # Stockage de l'arête dans une liste séparée (optionnel)
        edges.append((num_sommet1, num_sommet2, temps))