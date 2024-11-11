import MetroGetFile as mgf
import BFS as bfs
import Bellman as bll
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

#le plus court chemin
