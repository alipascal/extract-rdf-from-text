import os
import json
from dotenv import load_dotenv 

from rdflib import Graph, Namespace, RDF, URIRef

# ===== CONFIG =====

load_dotenv()
STANFORD_DIR = os.getenv("STANFORD_DIR") # crée un fichier .env et mets ton path de stanford dedans
INPUT_JSON = STANFORD_DIR + r"\tmplpp9z_bv.txt.json" # change le fichier enfonction de ce que stanford pipeline t'as généré
OUTPUT_RDF = "output.ttl"


EX = Namespace("http://example.org/")

VERB_MAP = {
    "write": "hasAuthor",
    "born": "bornIn",
    "locate": "locatedIn"
}

NER_CLASS = {
    "PERSON": "Person",
    "ORGANIZATION": "Organization",
    "WORK_OF_ART": "Work",
    "LOCATION": "Place",
    "STATE_OR_PROVINCE": "Place"
}

# ================= UTILS =================

def uri(text):
    return EX[text.replace(" ", "_")]


# TODO retour les entité mais pas les relations

# ================= PIPELINE =================

g = Graph()
g.bind("ex", EX)

with open(INPUT_JSON, encoding="utf-8") as f:
    data = json.load(f)

for sent in data["sentences"]:
    tokens = {t["index"]: t for t in sent["tokens"]}
    subject = None
    obj = None
    predicate = None

    # --- Entités ---
    for t in sent["tokens"]:
        if t["ner"] != "O":
            g.add((uri(t["word"]), RDF.type, uri(NER_CLASS.get(t["ner"], "Entity"))))

    # --- Relations ---
    for dep in sent["basicDependencies"]:
        gov = dep["governor"]
        dep_idx = dep["dependent"]

        if dep["dep"] == "nsubj":
            subject = tokens[dep_idx]["word"]

        if dep["dep"] in ["obj", "obl"]:
            obj = tokens[dep_idx]["word"]

        if dep["dep"] == "ROOT":
            lemma = tokens[dep_idx]["lemma"]
            if lemma in VERB_MAP:
                predicate = VERB_MAP[lemma]

    if subject and obj and predicate:
        g.add((uri(obj), uri(predicate), uri(subject)))

# ================= SAVE =================

g.serialize(OUTPUT_RDF, format="turtle")
print("✅ RDF généré avec prédicat :", OUTPUT_RDF)