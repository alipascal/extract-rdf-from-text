# Text To RDF : Extraction Sémantique du Web 

Projet universitaire (Sujet 2) :
Extraction des entités à partir de texte et transformation en un graphe RDF

<p align="center">
  <img width="50%" alt="output_wikipedia_nltk_en" src="https://github.com/user-attachments/assets/3b0c7183-9731-4e95-b80a-7ab5c380cd62" />
</p>

Ce projet implémente différents modèles de NER (Named-Entity Recognition) et d'extraction de triplets RDF (sujet, prédicat, objet).

Quatres modèles sont présentés : 
- SpaCy
- OpenAI (gpt-5-nano)
- NLTK
- Stanford CoreNLP

Ces modèles sont testés sur des textes bruts non structurés.
Les corpus de textes proviennent d'articles scientifiques, de comptes rendus médicaux, d'articles de presse et d'extraits de pages Wikipédia.
Toutes les sources sont référencées dans les fichiers correspondants.

## Features

* Prend en entrée un fichier contenant du texte brute (paragraphes, phrases simples...) et retourne un graphe RDF.
* Visualisation du graphe à partir d'un fichier en html
* Génère un fichier XML (.rdf) et un fichier turtle (.ttl) pour le graphe.
* Traite du texte en anglais (et français pour les modèles d'OpenAI et SpaCy)

## How it works / Architecture

**Architecture générale :**

<p align="center">
  <img width="50%" alt="architecture" src="https://github.com/user-attachments/assets/cc4a989b-2262-4b6a-9cd6-f47266b727e3" />
</p>

## Installation & Setup projet pour le développement

### Dépendances

* Python ≥ 3.11
* Stanford CoreNLP ≥ 4.5.10
* OpenAI API key

### Setup

Le programme requiert les packages Python suivants :
- `rdflib` (==7.5.0) : Librairie pour manipuler et créer des graphes RDF
- `pyvis` : Visualisation interactive de graphes
- `nltk` (==3.9.2) : Toolkit de traitement du langage naturel
- `spacy` (==3.8.11) : NLP avancé pour tokenisation, entités nommées, etc.
- `openai` (==2.14.0) : Intégration des modèles OpenAI
- `python-dotenv` (==1.2.1) : Chargement des variables d’environnement depuis un fichier .env
- `numpy` (==2.4.0) : Librairie scientifique, utilisée ici pour supporter nltk

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
* `--lang` : langue du fichier d’entrée (`fr` ou `en`, par défaut `en`)
* `--output` : nom file sortir (par défaut `output`)

```bash
python main.py <model> --lang <fr/en> --file input.txt --output output
```

Le programme génère :
* un fichier `.rdf` au format XML
* un fichier `.ttl` au format Turtle
* un fichier `.html` pour la visualisation

!!! Les modèles NLTK et Stanford CoreNLP traitent uniquement les textes en anglais.

**Exemples d'utilisation :**

```bash
python main.py spacy --lang fr # SpaCy français sur le fichier par défaut
python main.py nltk --file mon_fichier.txt # NLTK sur un fichier spécifique
python main.py openai # OpenAI
```

## Auteurs

[@hacjoseph](https://github.com/hacjoseph)

[@imane-hashCode](https://github.com/imane-hashCode)

[@alipascal](https://github.com/alipascal)


## License

Ce projet est sous licence MIT – une licence open source permissive qui permet l’utilisation, la modification et la distribution gratuites du logiciel.

Pour plus de détails, voir la documentation [MIT License](https://opensource.org/licenses/MIT).
