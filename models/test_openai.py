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


def extractTriplets_openai(text):
  # Load the .env file
  load_dotenv()
  # Get API key from environment variable
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

  functions = [
    {
      "name": "extract_triplets",
      "description": "Extraire le ou les triplets (sujet, prédicat, objet) depuis un texte. Utiliser le nom générique sans article si possible. Passer les verbes et prédicat au présent.",
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

  client = OpenAI(api_key=OPENAI_API_KEY)

  response = client.chat.completions.create(
      model="gpt-5-nano", # fais gaffe change ps le model sinon ça va coûter plus cher pour moi ;-;
      messages=[
          {
              "role": "user",
              "content": f"Extrais tous les triplets du texte suivant : {text}"
          }
      ],
      functions=functions,
      function_call={"name": "extract_triplets"}
  )

  triplets = response.choices[0].message.function_call.arguments
  triplets = json.loads(triplets)
  print(triplets)

  entities = dict_to_list(triplets)
  
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

