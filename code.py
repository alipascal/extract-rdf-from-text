import spacy
from rdflib import Graph, URIRef, Literal, Namespace

nlp = spacy.load("fr_core_news_sm")

EX = Namespace("http://example.org/")

def text_to_rdf(text):
    doc = nlp(text)
    g = Graph()

    for sent in doc.sents:
        subj = None
        verb = None
        obj = None

        for token in sent:
            if token.dep_ == "nsubj":
                subj = token.text
            if token.pos_ == "VERB":
                verb = token.lemma_
            if token.dep_ in ("obj", "obl"):
                obj = token.text

        if subj and verb and obj:
            g.add((
                URIRef(EX[subj.replace(" ", "_")]),
                URIRef(EX[verb]),
                Literal(obj)
            ))

    return g

# Test
text = "Marie Curie a découvert le polonium."
rdf_graph = text_to_rdf(text)

print(rdf_graph.serialize(format="turtle"))
