from class_local import Address, Person, Company, Country
import networkx as nx
import matplotlib.pyplot as plt

def afficher_objet_depliable(objet):
    """
    Affiche un objet avec des attributs dépliables et repliables, positionnés correctement.

    Args:
        objet: L'objet Python à visualiser.
    """

    G = nx.DiGraph()
    nom_objet = type(objet).__name__
    G.add_node(nom_objet, type="objet", objet=objet, est_deplie=False)

    pos = {nom_objet: (0, 0)}

    def dessiner_graphe():
        plt.clf()
        nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')
        nx.draw_networkx_edges(G, pos, edge_color='gray')
        labels = {node: node for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
        plt.gcf().canvas.draw_idle()

    def deplier_attributs(noeud_parent):
        """Déplie les attributs d'un noeud, y compris les objets imbriqués."""
        node_data = G.nodes[noeud_parent]
        if "objet" in node_data:
            objet = node_data["objet"]
            if hasattr(objet, "__dict__"):
                n = len(objet.__dict__)
                for i, (nom, valeur) in enumerate(objet.__dict__.items()):
                    nom_attribut = f"{noeud_parent}.{nom}"
                    if nom_attribut not in G:
                        G.add_node(nom_attribut, type="attribut", valeur=valeur, est_deplie=False)
                        G.add_edge(noeud_parent, nom_attribut)
                        pos[nom_attribut] = (pos[noeud_parent][0] + 1, pos[noeud_parent][1] - n / 2 + i)
                        if hasattr(valeur, "__dict__") or isinstance(valeur, (list, tuple, dict)):
                            G.nodes[nom_attribut]['objet'] = valeur  # On garde l'objet pour les déploiements futurs
            elif isinstance(objet, (list, tuple, dict)):
                n = len(objet)
                for i, valeur in enumerate(objet):
                    nom_attribut = f"{noeud_parent}[{i}]"
                    if nom_attribut not in G:
                        G.add_node(nom_attribut, type="element", valeur=valeur, est_deplie=False)
                        G.add_edge(noeud_parent, nom_attribut)
                        pos[nom_attribut] = (pos[noeud_parent][0] + 1, pos[noeud_parent][1] - n / 2 + i)
                        if hasattr(valeur, "__dict__") or isinstance(valeur, (list, tuple, dict)):
                            G.nodes[nom_attribut]['objet'] = valeur

    def replier_attributs(noeud_parent):
        """Replie les attributs d'un noeud, y compris les objets imbriqués."""
        noeuds_a_supprimer = []
        for noeud in G.nodes():
            if noeud.startswith(noeud_parent + ".") or noeud.startswith(noeud_parent + "["):
                noeuds_a_supprimer.append(noeud)
        for noeud in noeuds_a_supprimer:
            del pos[noeud]
            G.remove_node(noeud)
        # Récursivement replier les attributs des objets imbriqués
        for noeud in list(G.nodes()):  # Important de faire une copie de la liste
            if noeud.startswith(noeud_parent + ".") or noeud.startswith(noeud_parent + "["):
                if G.nodes[noeud].get("est_deplie", False):
                    replier_attributs(noeud)

    def onclick(event):
        if event.inaxes:
            for node, (x, y) in pos.items():
                if abs(event.xdata - x) < 0.1 and abs(event.ydata - y) < 0.1:
                    if G.nodes[node].get("est_deplie", False):
                        G.nodes[node]["est_deplie"] = False
                        replier_attributs(node)
                    else:
                        G.nodes[node]["est_deplie"] = True
                        deplier_attributs(node)
                    dessiner_graphe()
                    attributs = nx.get_node_attributes(G, "valeur")
                    if node in attributs:
                        print(f"Attribut: {node}, Valeur: {attributs[node]}")
                    else:
                        print(f"Noeud: {node}")
                    break

    plt.gcf().canvas.mpl_connect('button_press_event', onclick)
    dessiner_graphe()
    plt.show()

entreprise = Company(
    name="Tech Innovators",
    employees=[
        Person(
            name="Jean Dupont",
            age=30,
            address=Address(
                street="123 Rue de Paris",
                city="Paris",
                postal_code="75001",
                country=Country(name="France", code="FR")
            )
        )
    ]
)
afficher_objet_depliable(entreprise)