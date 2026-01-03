# Text To RDF : Extraction Sémantique du Web 

Projet universitaire - Sujet 2 :
Extraction des entités à partir de texte et transformation en un graphe RDF

Ce projet implémente différents modèles de NER (Named-Entity Recognition) et d'extraction de triplets RDF (sujet, prédicat, objet).

4 modèles sont présentés : SpaCy, OpenAI (gpt-5-nano), NLTK, et Stanford CoreNLP.

Ces modèles sont testés sur des textes bruts non structurés.
Les corpus proviennent d'articles scientifiques, de comptes rendus médicaux, d'articles de presse et d'extraits de pages Wikipédia.

Toutes les sources sont référencées dans les fichiers correspondants.


## Installation & Setup projet pour le développment

Environement virtuel sur Windows :
```bash
python -m venv venv # création
.\venv\Scripts\activate # activation
deactivate # désactivation
```

Environnement virtuel sur Linux :
```bash
python3 -m venv venv # création
source venv/bin/activate # activation
deactivate # désactivation
```

Installation des dépendances Python lorsque la ``venv`` est activée :
```bash
pip install -r requirements.txt
```


### Utilisation & Installation de SpaCy

Installation du model SpaCy français et anglais, avant le lancement du programme :
```bash
python -m spacy download fr_core_news_lg
python -m spacy download en_core_web_lg
```

Désinstalltion du model si besoin :
```bash
pip uninstall fr_core_news_lg
``` 

Documentations SpaCy : https://spacy.io/models/fr/#fr_core_news_sm


### Utilisation & installation de NLTK

Pour utiliser NLTK, il faut télécharger les ressources requises.

Soit en téléchargeant l’intégralité des modules :

```bash
python -c "import nltk; nltk.download('all')"
```

Soit en téléchargeant les modules spécifiques :

```bash
python -c "import nltk; nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('maxent_ne_chunker_tab'); nltk.download('words')"
```


### Utilisation de API OpenAI (chatGPT)

Créer et ajouter dans le fichier ``.env`` une clé API secrète OpenAI :
```.env
OPENAI_API_KEY=sk-XXX
```


### Utilisation & Installation de CoreNLP

Pour utiliser CoreNLP Stanford, il faut télécharger le modèle au format `.zip` depuis le site officel : https://stanfordnlp.github.io/CoreNLP/

Ensuite, ajouter dans le fichier ``.env`` le chemin absolu vers le dossier de CoreNLP, comme dans l'exemple ci-dessous :

```.env
STANFORD_DIR=C:\...\...\stanford-corenlp-4.5.10
```


## Lancement de l’application

Le programme s’exécute depuis l’invite de commande.

**Arguments :**

* `model` : le modèle à utiliser (`spacy`, `nltk`, `stanford`, `openai`)
* `--file` : fichier d’entrée (par défaut `input.txt`)
* `--lang` : langue du fichier d’entrée (`fr` ou `en`, par défaut `fr`)

```bash
python main.py <model> --lang <fr/en> --file input.txt
```

Le programme génère :
* un fichier `.rdf` au format XML
* un fichier `.ttl` au format Turtle

!!! Les modèles NLTK et Stanford CoreNLP traitent uniquement les textes en anglais.

**Exemples d'utilisation :**

```bash
python main.py spacy --lang fr # SpaCy français sur le fichier par défaut
python main.py nltk --file mon_fichier.txt # NLTK sur un fichier spécifique
python main.py openai # OpenAI
```

