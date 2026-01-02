import spacy
from rdflib import Graph, Namespace
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict
import re


class RDFTripleExtractor:
    """Extracteur de triplets RDF robuste multilingue (FR / EN)"""

    def __init__(self, lang: str = "fr"):
        """
        Initialise l'extracteur
        
        Args:
            lang: Langue du texte ("fr" ou "en")
        """
        assert lang in ("fr", "en"), "Langue doit être 'fr' ou 'en'"
        self.lang = lang

        # Charger spaCy
        print("Chargement de spaCy...")
        try:
            if self.lang == "fr":
                self.nlp = spacy.load("fr_core_news_lg")
                print("✓ Modèle français chargé")
            else:
                self.nlp = spacy.load("en_core_web_sm")
                print("✓ Modèle anglais chargé")
        except Exception as e:
            print(" Veuillez installer le modèle spaCy requis.")
            raise e

        # Initialiser graphe RDF
        self.rdf_graph = Graph()
        self.ex = Namespace("http://example.com/")
        self.rdf_graph.bind("ex", self.ex)

        print("✓ Système d'extraction initialisé")


    def extract_triplets_spacy(self, text: str) -> List[Dict]:
        """Extraction syntaxique basée sur spaCy + patterns"""
        doc = self.nlp(text)
        triplets = []

        # 1. Extraction syntaxique générique (nsubj, ROOT, obj/attr)
        for sent in doc.sents:
            subject = None
            predicate = None
            obj = None

            for token in sent:
                if token.dep_ in ("nsubj", "nsubj:pass"):
                    subject = " ".join([t.text for t in token.subtree])
                if token.pos_ == "VERB" and token.dep_ == "ROOT":
                    predicate = token.lemma_
                if token.dep_ in ("obj", "attr", "dobj", "pobj", "obl"):
                    obj = " ".join([t.text for t in token.subtree])

            if subject and predicate and obj:
                triplets.append((
                    self._clean_text(subject), predicate,self._clean_text(obj)
                ))

        return triplets

    def _clean_text(self, text: str) -> str:
        """Nettoie le texte (articles, ponctuation excessive)"""
        # Enlever articles au début (adapté FR/EN)
        if self.lang == "fr":
            text = re.sub(r"^(le|la|les|l'|un|une|des)\s+", "", text, flags=re.IGNORECASE)
        else:
            text = re.sub(r"^(the|a|an)\s+", "", text, flags=re.IGNORECASE)
        # Enlever ponctuation finale
        text = re.sub(r"[,;.!?]+$", "", text)
        return text.strip()

    def process_text(self, text: str) -> List[Dict]:
        """Pipeline complet d'extraction"""
        print(f"\n{'=' * 60}")
        print(f" ANALYSE DU TEXTE ({len(text)} caractères) — Langue: {self.lang}")
        print(f"{'=' * 60}")

        all_triplets = []

        # Extraction syntaxique
        spacy_triplets = self.extract_triplets_spacy(text)
        all_triplets.extend(spacy_triplets)
        print(f"   ✓ {len(spacy_triplets)} triplets trouvés")
        print(f"\n Total: {len(all_triplets)} triplets uniques extraits")

        return all_triplets


    def print_triplets(self, triplets: List[Dict]):
        """Affiche les triplets de manière lisible"""
        if not triplets:
            print("\n Aucun triplet trouvé")
            return

        print(f"\n TRIPLETS EXTRAITS ({len(triplets)}):")
        print("=" * 70)
        for i, t in enumerate(triplets, 1):

            print(f"\n{i}. Sujet: {t[0]}")
            print(f"   Prédicat: {t[1]}")
            print(f"   Objet: {t[2]}")

def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Exemple d'utilisation
# if __name__ == "__main__":
#     # Choisir langue "fr" ou "en"
#     extractor = RDFTripleExtractor(lang="fr")
    
#     text = read_text_file("texte.txt")

#     triplets = extractor.process_text(text)
#     print(triplets)
#     extractor.print_triplets(triplets)

