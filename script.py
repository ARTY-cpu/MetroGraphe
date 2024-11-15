from Bellman import bellman_ford
import MetroGetFile as mgf
import BFS as bfs
import Prim as prm

#création du graphe
graph, edge = mgf.lire_metro()


#vérification si connexe
if bfs.is_graph_connected(graph) :
    print("Le graphe est connexe")
else :
    print("Le graphe est non connexe")

#affichage de tous les sommets non connexes
for num_sommet, info in graph.items():
    if not info['voisins']:
        print(f"Attention : La station {info['nom']} (Sommet {num_sommet}) n'a aucun voisin.")


#Plus court chemin
chemin, temps_total = bellman_ford(graph, edge, "Carrefour Pleyel", "Villejuif, P. Vaillant Couturier")


# Afficher le chemin dans un fichier HTML 
chemin_détaillé = [{"nom": graph[station_id]["nom"], "ligne": graph[station_id]["ligne"]} for station_id in chemin]
afficher_chemin_en_html(chemin_détaillé, temps_total)

#ACPM
start_node = 0
acpm_edges = prm.Prim(graph, start_node)  # Récupérer les arêtes de l'ACPM

# Afficher l'ACPM
prm.afficher_acpm(acpm_edges, graph)  # Passer les arêtes de l'ACPM et le graphe
