# Projet Extraction Sémentique du Web - Sujet 2

Projet universitaire - Extraction des entités à partir de texte et transformation dans un graphe RDF

## Installation du projet pour le développment

Création de l'environement, Activation et désactivation de l'environement, sur Windows :
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
```bash
deactivate
```

Création de l'environement, Activation et désactivation de l'environement, sur Linux :
```bash

```
```bash

```
```bash

```

Installation des dépendances python :
```bash
pip install -r requirements.txt
```

### Utilisation de SpaCy

Installation du model SpaCy multi-langue avant le lancement du programme :
```bash
python -m spacy download xx_ent_wiki_sm
```

Désinstalltion du model si besoin :
```bash
pip uninstall xx_ent_wiki_sm
``` 

Documentations SpaCy : https://spacy.io/models/fr/#fr_core_news_sm

### Utilisation de API OpenAI (chatGPT)

Créer un fichier ``.env`` contenant la clé API secrète :
```.env
OPENAI_API_KEY=sk-XXX
```