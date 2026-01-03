"""
Code Test - Inspirer de code /test1.py
"""
import argparse

import re
import unicodedata

from rdflib import Graph, URIRef, Literal, Namespace

from models.code_openai import extractTriplets_openai
from models.code_spacy import RDFTripleExtractor
from models.pipeline_nltk import extractTriplets_nltk
from models.pipeline_stanford import extractTriplets_stanford


EX = Namespace("http://example.org/")
def createRDFNode(subj, verb, obj):
    return URIRef(EX[subj]), URIRef(EX[verb]), Literal(obj)


def cleanEntity(subj, verb, obj):
    
    def remove_accents(text):
        # Retirer les accents
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )

    def clean(text):
        # Retirer les caractères spéciaux
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        return text.replace(" ", "_")
    
    subj, verb, obj = tuple(map(remove_accents, (subj, verb, obj)))
    subj, verb, obj = tuple(map(clean, (subj, verb, obj)))

    return subj, verb, obj



def extractTriplets_example(text:str) -> list:
    # Exemple
    entities = [
        ("Marie Curie", "découvrir", "polonium"),
        ("roman", "ecrit par", "Agatha Christie"),
        ("médecin", "prescrire", "traitement"),
        ("patient", "prendre", "médicament"),
        ("Le Crime de l'Orient Express", "est", "roman"),
        ("Crime de l'Orient Express", 'est écrit par', 'Agatha Christie')
    ]
    return entities


def extractTriplets_spacy(text:str) -> list:
    extractor = RDFTripleExtractor(lang="fr")
    triplets = extractor.process_text(text)
    return triplets


def getFile(namefile:str) -> str:
    content = ""
    with open(namefile, "r", encoding="utf-8") as file:
        content = file.read()
    content = "".join(line for line in content.splitlines(True) if not line.startswith("#"))
    print("✓ Fichier input traité")
    return content



if __name__ == '__main__':
    # Text to RDF graph

    parser = argparse.ArgumentParser()
    parser.add_argument("model", choices=["spacy", "nltk", "stanford", "openai"])
    parser.add_argument("--file", default="input.txt")
    args = parser.parse_args()


    ACTIONS = {
        "spacy": extractTriplets_spacy,
        "nltk": extractTriplets_nltk,
        "stanford": extractTriplets_stanford,
        "openai": extractTriplets_openai,
        "example": extractTriplets_example,
    }


    method = args.model
    namefile = args.file
    text = getFile(namefile)
    print(f"¤ Exécution algorithme '{method}'")
    entities = ACTIONS[method](text)
    print(f"✓ Exécution algorithme '{method}' terminée")
    
    graph = Graph()
    for subj, verb, obj in entities:
        subj, verb, obj = cleanEntity(subj, verb, obj)
        node = createRDFNode(subj, verb, obj)
        graph.add(node)
    graph.serialize(destination="output.ttl", format="turtle")
    graph.serialize(destination="output.rdf", format="xml")
    print("✓ Fichier output créé")
    # pour visualiser le graphe : https://www.ldf.fi/service/rdf-grapher 

