import heapq

def Prim(graph, start):
    # Initialisation des structures de données
    visited = set()  # Garde les sommets déjà inclus dans l'ACPM
    edges = []       # Contiendra les arêtes de l'ACPM
    min_heap = []    # Tas pour stocker les arêtes triées par poids

    # Démarre avec le sommet de départ en marquant le coût initial à 0
    visited.add(start)
    for neighbor, weight in graph[start]['voisins']:
        heapq.heappush(min_heap, (weight, start, neighbor))

    # Tant que l'ACPM n'est pas complet
    while min_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue

        # Ajoute l'arête à l'arbre couvrant minimal
        visited.add(v)
        edges.append((u, v, weight))

        # Ajoute les nouvelles arêtes au tas
        for neighbor, weight in graph[v]['voisins']:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, v, neighbor))
    
    return edges


def afficher_acpm(acpm_edges, graph):
    total_weight = 0
    print("Arbre couvrant de poids minimum")
    for u, v, weight in acpm_edges:
        station_u = graph[u]['nom']
        station_v = graph[v]['nom']
        print(f"{station_u} - {station_v} avec un poids de {weight} secondes")
        total_weight += weight  # Ajoute le poids de l'arête au poids total
    print(f"Poids total de l'ACPM : {total_weight} secondes")

def generer_acpm(graph):
    # Récupère un sommet de départ arbitraire
    start = next(iter(graph))
    acpm_edges = Prim(graph, start)
    afficher_acpm(acpm_edges, graph)
