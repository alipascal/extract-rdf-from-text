import subprocess
import json
import os
import tempfile


from dotenv import load_dotenv 

load_dotenv()
STANFORD_DIR = os.getenv("STANFORD_DIR")



def process_texts(texts):

    # -------- 1. Un seul fichier texte --------
    full_text = "\n".join(texts)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write(full_text)
        input_file = f.name

    # -------- 2. Commande Stanford --------
    cmd = [
        "java", "-mx4g", "-cp", "*",
        "edu.stanford.nlp.pipeline.StanfordCoreNLP",
        "-annotators", "tokenize,ssplit,pos,lemma,ner,depparse",
        "-file", input_file,
        "-outputFormat", "json"
    ]

    subprocess.run(cmd, cwd=STANFORD_DIR, stdout=subprocess.DEVNULL)

    # -------- 3. Lecture du JSON UNIQUE --------
    output_file = os.path.basename(input_file) + ".json"

    with open(os.path.join(STANFORD_DIR, output_file), encoding="utf-8") as f:
        data = json.load(f)

    relations = set()


    # -------- 4. Parcours des phrases --------
    for sentence in data["sentences"]:

        entities = {}

        # --- NER ---
        for token in sentence["tokens"]:
            if token["ner"] != "O":
                entities[token["index"]] = token["word"]

        # --- Relations ---
        for dep in sentence["basicDependencies"]:
            if dep["dep"].startswith("nsubj"):
                verb = dep["governorGloss"]
                subj_idx = dep["dependent"]

                for d in sentence["basicDependencies"]:
                    if d["governor"] == dep["governor"] and d["dep"].startswith(("obj", "obl")):
                        obj_idx = d["dependent"]

                        if subj_idx in entities and obj_idx in entities:
                            relations.add((
                                entities[subj_idx],
                                verb.lower(),
                                entities[obj_idx]
                            ))

    return list(relations)


def extractTriplets_stanford(text:str, lang="en"):
    assert lang == "en", "Langue doit être anglais ('en')"
    # On crée une liste de phrases
    list_text = text.split(".")[:-1]
    return process_texts(list_text)


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    texts = [
        "Agatha Christie wrote the novel Murder on the Orient Express.",
        "Google is located in California.",
        "Barack Obama was born in Hawaii.",
        "The patient has diabetes."
    ]

    results = process_texts(texts)

    print("\nRelations extraites (JSON unique) :")
    for r in results:
        print(r)
