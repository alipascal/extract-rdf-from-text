"""
Visualisation RDF avec PyVis
"""

from rdflib import Graph, RDF, RDFS, OWL, URIRef, Literal
from pyvis.network import Network
import matplotlib.pyplot as plt


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
    print(f"✓ Visualisation créée : {output}")
    

if __name__ == "__main__":
    visualize_rdf("output.rdf")