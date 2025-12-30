"""
Code chatGPT test pour trouver l'inspiration
"""

import spacy
from rdflib import Graph, URIRef, Literal, Namespace


EX = Namespace("http://example.org/")


def print_info_token(token):
    print(f"""
    TEXT        : {token.text}
    LEMMA       : {token.lemma_}
    POS         : {token.pos_}
    TAG         : {token.tag_}
    DEP         : {token.dep_}

    HEAD        : {token.head.text}
    CHILDREN    : {[child.text for child in token.children]}

    SUBTREE     : {[t.text for t in token.subtree]}

    ENT TYPE    : {token.ent_type_}
    IS STOP     : {token.is_stop}
    IS PUNCT    : {token.is_punct}
    LIKE NUM    : {token.like_num}
    
    ------------------------------------------
    """)


nlp = spacy.load("fr_core_news_sm")

def extractTriplets_spacy(text):
    # test SpaCy
    triplets = []
    doc = nlp(text)

    for sent in doc.sents:
        subj, verb, obj = None, None, None

        for token in sent:
            print_info_token(token)
            if token.dep_ == "nsubj":
                subj = token.text
            if token.pos_ == "VERB":
                verb = token.lemma_
            if token.dep_ in ("obj", "obl"):
                obj = token.text

        if subj and verb and obj:
            triplets.append((subj, verb, obj))
            
    return triplets


# Test
# text = "Le patient prend un médicament. Le médecin prescrit un traitement." 
# text = "Marie Curie a découvert le polonium."
text = "Le Crime de l'Orient Express est un roman écrit par Agatha Christie." # erreur
# text = "Le Crime de l'Orient Express est un roman. Le roman a été écrit par Agatha Christie." # erreur
# text = "Le Crime est un roman. Le roman a été écrit par Agatha Christie." # erreur
# text = "Le Crime est un roman. Agatha Christie écrit un roman." # incomplet

entities = extractTriplets_spacy(text)
print(entities)
