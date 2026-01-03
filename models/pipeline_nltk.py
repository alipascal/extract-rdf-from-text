import nltk
from nltk import word_tokenize, pos_tag, ne_chunk


# =========================
# ÉTAPE 3 : PRÉTRAITEMENT
# =========================
def step3_preprocess(text):
    """
    Prend un texte brut (n'importe lequel)
    Retourne :
        - tokens
        - pos_tags
    """
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return tokens, pos_tags


# =========================
# ÉTAPE 4 : NER
# =========================
def step4_ner(pos_tags):
    """
    Prend les pos_tags (étape 3)
    Retourne une liste d'entités détectées
    """
    tree = ne_chunk(pos_tags)
    entities = []

    for node in tree:
        if hasattr(node, "label"):
            entity = " ".join(word for word, pos in node.leaves())
            label = node.label()
            entities.append((entity, label))

    return entities


# =========================
# ÉTAPE 5 : RELATIONS
# =========================
def step5_relations(tokens, pos_tags, entities):
    """
    Prend :
        - tokens
        - pos_tags
        - entités
    Retourne :
        - liste de tuples (sujet, relation, objet)
    """
    relations = []

    # positions des entités dans la phrase
    sentence = " ".join(tokens)

    for i, (word, tag) in enumerate(pos_tags):
        # verbe = relation
        # TODO détecter les verbes composés
        if tag.startswith("VB"):
            relation = word.lower()

            subject = None
            obj = None

            # entité avant le verbe
            for ent, label in entities:
                if ent in " ".join(tokens[:i]):
                    subject = ent

            # entité après le verbe
            for ent, label in entities:
                if ent in " ".join(tokens[i + 1:]):
                    obj = ent
                    break

            if subject and obj:
                relations.append((subject, relation, obj))

    return relations


# =========================
# PIPELINE COMPLET
# =========================
def process_text(text):
    """
    UNE SEULE MÉTHODE À APPELER
    """
    tokens, pos_tags = step3_preprocess(text)
    entities = step4_ner(pos_tags)
    relations = step5_relations(tokens, pos_tags, entities)
    return relations


def extractTriplets_nltk(text:str, lang="en") -> list:
    entities = []
    # Traiter le texte phrase par phrase
    for sentence in text.split("."):
        if sentence == "":
            continue
        entities.extend(process_text(sentence))
    return entities


# =========================
# MAIN (TEST)
# =========================
if __name__ == "__main__":

    texts = [
        "Agatha Christie wrote the novel Murder on the Orient Express.",
        "Google is located in California.",
        "Barack Obama was born in Hawaii.",
        "The patient has diabetes."
    ]

    for t in texts:
        print("\nTexte :", t)
        print("Relations extraites :", process_text(t))
