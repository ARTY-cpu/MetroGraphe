from collections import deque

def is_graph_connected(graph):
    # découverte de tous les sommets à partir du sommet 0
    start_station = list(graph.keys())[0]
    visited = set()  # Ensemble pour garder les stations visitées
    queue = deque([start_station])

    while queue:
        station = queue.popleft()
        if station not in visited:
            visited.add(station)
            # Ajouter toutes les stations voisines de celle-ci dans la file
            for neighbor, _ in graph[station]['voisins']:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    # Vérifier si toutes les stations ont été visitées
    return len(visited) == len(graph)