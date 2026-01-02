"""
Code Test - Inspirer de code /test1.py
"""

from rdflib import Graph, URIRef, Literal, Namespace

import re
import unicodedata


EX = Namespace("http://example.org/")
def createRDFNode(subj, verb, obj):
    return URIRef(EX[subj]), URIRef(EX[verb]), Literal(obj)


def cleanEntity(subj, verb, obj):
    
    def clean(text):
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        return text.replace(" ", "_")
    
    def remove_accents(text):
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
    
    subj, verb, obj = tuple(map(clean, (subj, verb, obj)))
    subj, verb, obj = tuple(map(remove_accents, (subj, verb, obj)))

    return subj, verb, obj



def extractTriplets(text):
    # TODO
    entities = [
        ("Marie Curie", "découvrir", "polonium"),
        ("roman", "estUn", "Le Crime de l Orient Express"),
        ("roman", "ecritPar", "Agatha Christie"),
        ("médecin", "prescrire", "traitement"),
        ("patient", "prendre", "médicament"),
        ("Le Crime de l'Orient Express", "est", "roman"),
        ("Crime de l'Orient Express", 'est écrit par', 'Agatha Christie')
    ]
    return entities



def getFichier(nom_fichier):
    # code de jospeh 
    # traite input.txt
    return "None"



if __name__ == '__main__':
    # Text to RDF graph
    graph = Graph()
    text = getFichier("nom_du_fichier")
    # Traiter le texte phrase par phrase
    for sentence in text.split("."):
        if sentence == "":
            continue
        entities = extractTriplets(sentence)
        for subj, verb, obj in entities:
            subj, verb, obj = cleanEntity(subj, verb, obj)
            node = createRDFNode(subj, verb, obj)
            graph.add(node)
    graph.serialize(destination="output.ttl", format="turtle")
    # pour visualiser le graphe : https://www.ldf.fi/service/rdf-grapher 


