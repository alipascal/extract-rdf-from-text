"""
Code Test - Inspirer de code /test1.py
"""

import spacy
from rdflib import Graph, URIRef, Literal, Namespace


EX = Namespace("http://example.org/")
def createRDFNode(subj, verb, obj):
    return URIRef(EX[subj]), URIRef(EX[verb]), Literal(obj)


import re
def cleanEntity(subj, verb, obj):

    def clean(text):
        text = re.sub(r'[^\x20-\x7E]', '', text)
        return text.replace(" ", "_")
    
    return clean(subj), clean(verb), clean(obj)


def extractTriplets(text):
    # TODO
    entities = [
        ("Marie Curie", "découvrir", "polonium"),
        ("roman", "estUn", "Le Crime de l Orient Express"),
        ("roman", "ecritPar", "Agatha Christie"),
        ("médecin", "prescrire", "traitement"),
        ("patient", "prendre", "médicament"),
        ("Le Crime de l'Orient Express", "est", "roman"),
        ("Le Crime de l'Orient Express", "a été écrit par", "Agatha Christie")
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
    entities = extractTriplets(text)
    for subj, verb, obj in entities:
        subj, verb, obj = cleanEntity(subj, verb, obj)
        node = createRDFNode(subj, verb, obj)
        graph.add(node)
    graph.serialize(destination="output.rdf", format="turtle")
    # pour visualiser le graphe : https://www.ldf.fi/service/rdf-grapher 
