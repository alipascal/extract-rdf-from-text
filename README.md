# Projet Extraction Sémentique du Web - Sujet 2

Projet universitaire - Extraction des entités à partir de texte et transformation dans un graphe RDF

## Installation du projet pour le développment

Création de l'evironement
```bash
python -m venv venv
```

Activation et désactivation de l'environement
```bash
.\venv\Scripts\activate # windoaws
```
```bash
deactivate # windoaws
```

Installation des dépendances python :
```bash
pip install -r .\requirements.txt
```

Installation du model SpaCy multi-langue avant le lancement du programme :
```bash
python -m spacy download xx_ent_wiki_sm
```
