import subprocess
import json
import os
import tempfile

from dotenv import load_dotenv 

load_dotenv()
STANFORD_DIR = os.getenv("STANFORD_DIR")


def process_text(text):
    """
    Pipeline complet Stanford :
    entrée : texte brut
    sortie : liste de tuples (sujet, relation, objet)
    """

    # fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write(text)
        input_file = f.name

    # commande Stanford
    cmd = [
        "java", "-mx4g", "-cp", "*",
        "edu.stanford.nlp.pipeline.StanfordCoreNLP",
        "-annotators", "tokenize,ssplit,pos,lemma,ner,depparse",
        "-file", input_file,
        "-outputFormat", "json"
    ]

    # exécution
    subprocess.run(cmd, cwd=STANFORD_DIR, stdout=subprocess.DEVNULL)

    # lecture du résultat
    output_file = os.path.basename(input_file) + ".json"

    with open(os.path.join(STANFORD_DIR, output_file), encoding="utf-8") as f:
        data = json.load(f)


    relations = []

    for sentence in data["sentences"]:
        entities = {}

        # ---------- ÉTAPE 4 : NER ----------
        for token in sentence["tokens"]:
            if token["ner"] != "O":
                entities[token["index"]] = token["word"]

        # ---------- ÉTAPE 5 : RELATIONS ----------
        for dep in sentence["basicDependencies"]:
            if dep["dep"] in ["nsubj", "nsubjpass"]:
                verb = dep["governorGloss"]
                subj_idx = dep["dependent"]

                # chercher un objet
                for d in sentence["basicDependencies"]:
                    if d["governor"] == dep["governor"] and d["dep"] in ["dobj", "nmod", "obl"]:
                        obj_idx = d["dependent"]

                        if subj_idx in entities and obj_idx in entities:
                            relations.append((
                                entities[subj_idx],
                                verb.lower(),
                                entities[obj_idx]
                            ))

    return relations



def extractTriplets_stanford(text:str, lang="en") -> list:
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
        print("Relations :", process_text(t))
