def bellman_ford(graph, edges, nom_depart, nom_arrivee):
        # Créer le dictionnaire nom_to_id pour retrouver les IDs à partir des noms
        nom_to_id = {info['nom']: station_id for station_id, info in graph.items()}

        # Conversion des noms de stations en IDs
        depart = nom_to_id.get(nom_depart)
        arrivee = nom_to_id.get(nom_arrivee)

        # Vérification si les stations existent
        if depart is None or arrivee is None:
            print("Erreur : station de départ ou de destination introuvable.")
            return None

        # Initialisation des distances et des prédécesseurs
        distances = {station: float('inf') for station in graph}
        distances[depart] = 0
        predecesseurs = {station: None for station in graph}

        # Nombre de sommets dans le graphe
        n = len(graph)

        # Détendre toutes les arêtes |V| - 1 fois
        for _ in range(n - 1):
            for (u, v, temps) in edges:
                if distances[u] + temps < distances[v]:
                    distances[v] = distances[u] + temps
                    predecesseurs[v] = u
                if distances[v] + temps < distances[u]:
                    distances[u] = distances[v] + temps
                    predecesseurs[u] = v

        # Vérification de cycle de poids négatif (optionnel)
        for (u, v, temps) in edges:
            if distances[u] + temps < distances[v]:
                raise ValueError("Le graphe contient un cycle de poids négatif.")

        # Reconstruire le chemin le plus court
        chemin = []
        current = arrivee
        while current is not None:
            chemin.insert(0, current)
            current = predecesseurs[current]

        # Afficher le résultat
        if distances[arrivee] == float('inf'):
            print("Il n'y a pas de chemin entre", nom_depart, "et", nom_arrivee)
            return None

        print("Chemin le plus court de", nom_depart, "à", nom_arrivee, ":")
        for station in chemin:
            print("-", graph[station]['nom'], "(Ligne", graph[station]['ligne'], ")")
        print("Temps total estimé :", distances[arrivee], "secondes")

        return chemin, distances[arrivee]
