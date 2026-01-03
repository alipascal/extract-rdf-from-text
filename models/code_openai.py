"""
Function Calling avec OpenAI models
"""
import os
from dotenv import load_dotenv
import json

from openai import OpenAI


def dict_to_list(d:dict) -> list:
  result = [
    (t["subject"], t["predicate"], t["object"]) for t in d["triplets"]
  ]
  return result


def extractTriplets_openai(text:str, lang="fr") -> list:
  # Load the .env file
  load_dotenv()
  # Get API key from environment variable
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

  prompt = {
    "fr": "Extraire un triplet ou plusieurs (sujet, prédicat, objet) depuis un texte. Utiliser le nom générique sans article ('le', 'la', 'un', 'une') si possible. Mettre les verbes et prédicats au présent.",
    "en": "Extract a triplet or more (subject, predicate, object) from the text. Use the generic noun form without any article ('a', 'an', 'the'). Convert verbs in present tense."
  }

  functions = [
    {
      "name": "extract_triplets",
      "description": prompt[lang],
      "parameters": {
        "type": "object",
        "properties": {
          "triplets": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "subject": { "type": "string" },
                "predicate": { "type": "string" },
                "object": { "type": "string" }
              },
              "required": ["subject", "predicate", "object"]
            }
          }
        },
        "required": ["triplets"]
      }
    }
  ]

  entities = []
  client = OpenAI(api_key=OPENAI_API_KEY)

  print("¤ Exécution des requêtes API OpenAI")
  # Traiter le texte phrase par phrase
  for sentence in text.split("."):
    if sentence == "":
        continue
    response = client.chat.completions.create(
        model="gpt-5-nano", # fais gaffe change ps le model sinon ça va coûter plus cher pour moi ;-;
        messages=[
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        functions=functions,
        function_call={"name": "extract_triplets"}
    )
    triplets = response.choices[0].message.function_call.arguments
    triplets = json.loads(triplets)
    # print(triplets)
    temp = dict_to_list(triplets)
    entities.extend(temp)
  
  print("✓ Exécution des requêtes API OpenAI terminée")
  
  return entities



if __name__ == '__main__':
  # Test Input
  # text = "Le Crime de l'Orient Express est un roman écrit par Agatha Christie."
  # text = "Le Crime de l'Orient Express est un roman. Le roman a été écrit par Agatha Christie."
  # text = "Le patient prend un médicament." 
  # text = "Le médecin prescrit un traitement."
  # text = "Marie Curie a découvert le polonium."
  text = "Pierre affirme qu'il possède dans les rayons de sa bibliothèque le roman d'Agatha Christie, intitulé “Le Crime de l'Orient Express”." # erreur (mais exemple hyper compliquer)

  triplets = extractTriplets_openai(text)
  # triplets = {"triplets":[{"subject":"Crime de l'Orient Express","predicate":"est","object":"roman"},{"subject":"Roman","predicate":"est écrit par","object":"Agatha Christie"}]}
  # triplets = {'triplets': [{'subject': 'médecin', 'predicate': 'prescrit', 'object': 'traitement'}]}
  
  print(triplets)

