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
chemin, temps_total = bellman_ford(graph, edges, "Carrefour Pleyel", "Villejuif, P. Vaillant Couturier")


#ACPM
start_node = 0
acpm_edges = prm.Prim(graph, start_node)  # Récupérer les arêtes de l'ACPM

# Afficher l'ACPM
prm.afficher_acpm(acpm_edges, graph)  # Passer les arêtes de l'ACPM et le graphe
