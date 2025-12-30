"""
Code Test - Inspirer de code /test1.py
"""

import spacy
from rdflib import Graph, URIRef, Literal, Namespace


EX = Namespace("http://example.org/")
def createRDFNode(subj, verb, obj):
    return URIRef(EX[subj]), URIRef(EX[verb]), Literal(obj)


import re
import unicodedata
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


nlp = spacy.load("fr_core_news_sm")
def extractTriplets_spacy(text):
    # test SpaCy
    triplets = []
    doc = nlp(text)

    for sent in doc.sents:
        subj, verb, obj = None, None, None

        for token in sent:
            if token.dep_ == "nsubj":
                subj = token.text
            if token.pos_ == "VERB":
                verb = token.lemma_
            if token.dep_ in ("obj", "obl"):
                obj = token.text

        if subj and verb and obj:
            triplets.append((subj, verb, obj))
            
    return triplets


if __name__ == '__main__':
    # Text to RDF graph
    graph = Graph()
    text = "None"
    # Traiter le text phrase par phrase
    for sentence in text.split("."):
        if sentence == "":
            continue
        entities = extractTriplets(sentence)
        for subj, verb, obj in entities:
            subj, verb, obj = cleanEntity(subj, verb, obj)
            node = createRDFNode(subj, verb, obj)
            graph.add(node)
    graph.serialize(destination="output.rdf", format="turtle")
    # pour visualiser le graphe : https://www.ldf.fi/service/rdf-grapher 
