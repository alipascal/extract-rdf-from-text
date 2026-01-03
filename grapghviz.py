"""
Visualisation RDF avec PyVis
"""

from rdflib import Graph, RDF, RDFS, OWL, URIRef, Literal
from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx

IGNORED_PREDICATES = {
    RDF.type,
    RDFS.label
}

def short(uri):
    return str(uri).split('/')[-1].split('#')[-1].replace('_', ' ')

def visualize_rdf(rdf_file, output="graph.html"):
    g = Graph()
    g.parse(rdf_file)

    net = Network(
        height="100vh",
        width="100%",
        bgcolor="#1e1e1e",
        font_color="white",
        # directed=True
    )
    # net.barnes_hut()
    
    net.set_options("""
    {
      "physics": {
        "enabled": true,
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {
          "gravitationalConstant": -120,
          "centralGravity": 0.01,
          "springLength": 120,
          "springConstant": 0.08
        },
        "stabilization": {
          "iterations": 200
        }
      },
      "nodes": {
        "font": {
          "size": 20,
           "face": "arial"
        },
        "shape": "dot"
      },
      "edges": {
        "font": {
          "size": 14
        }
        
      }
    }
    """)

    nodes = set()

    for s, p, o in g:
        # Ignorer triplets techniques
        if p in IGNORED_PREDICATES:
            continue

        if not isinstance(o, URIRef):
            continue

        subj = short(s)
        pred = short(p)
        obj  = short(o)

        if subj not in nodes:
            net.add_node(
                subj,
                label=subj,
                color="#4CAF50",
                size=30
            )
            nodes.add(subj)

        if obj not in nodes:
            net.add_node(
                obj,
                label=obj,
                color="#2196F3",
                size=30
            )
            nodes.add(obj)

        net.add_edge(
            subj,
            obj,
            label=pred,
            title=pred,
            arrows="to",
            # font={"size": 16}
        )

    net.write_html(output)
    print(f"✅ Visualisation créée : {output}")
    

def visualize_rdf_png(rdf_file, output="graph.png"):
    g = Graph()
    g.parse(rdf_file)

    G = nx.DiGraph()

    for s, p, o in g:
        s_label = str(s).split("/")[-1].replace("_", " ")
        p_label = str(p).split("/")[-1].replace("_", " ")
        o_label = str(o).split("/")[-1].replace("_", " ")

        # Ignorer rdf:type pour la lisibilité
        if p_label == "type":
            continue

        G.add_edge(s_label, o_label, label=p_label)

    plt.figure(figsize=(16, 16))

    pos = nx.spring_layout(G, k=1.2, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="#A5D6A7",
        font_size=10,
        font_weight="bold",
        edge_color="#555555"
    )

    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=9
    )

    plt.title("Graphe RDF extrait du texte", fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output, dpi=300)
    plt.close()

    print(f"✅ PNG généré : {output}")

if __name__ == "__main__":
    visualize_rdf("output.rdf")
    visualize_rdf_png("output.rdf", output="graph.png")