import csv

def lire_metro():
    graph = {}
    edges = []
    with open("metro_old.txt", "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        
        # Traitement des sommets
        for line in reader:
            if line[0] == 'V':
                # Lecture d'un sommet
                num_sommet = int(line[1])
                nom_sommet = line[2]
                numero_ligne = line[3]
                si_terminus = line[4] == "True"  # Convertit en booléen
                branchement = int(line[5])
                
                # Ajout du sommet dans le graphe
                graph[num_sommet] = {
                    'nom': nom_sommet,
                    'ligne': numero_ligne,
                    'terminus': si_terminus,
                    'branchement': branchement,
                    'voisins': []
                }
            
            elif line[0] == 'E':
                # Lecture d'une arête
                num_sommet1 = int(line[1])
                num_sommet2 = int(line[2])
                temps = int(line[3])
                
                # Ajout de l'arête dans les voisins de chaque sommet
                graph[num_sommet1]['voisins'].append((num_sommet2, temps))
                graph[num_sommet2]['voisins'].append((num_sommet1, temps))
                
                # Stockage de l'arête dans une liste séparée
                edges.append((num_sommet1, num_sommet2, temps))

    return graph, edges