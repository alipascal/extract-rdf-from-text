"""
Testing Function Calling avec OpenAI models
"""
from dotenv import load_dotenv
import os

from openai import OpenAI


# Load the .env file
load_dotenv()
# Get API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def extractTriplets_openai(text):

    functions = [
      {
        "name": "extract_triples",
        "description": "Extraire des triplets (sujet, prédicat, objet) depuis un texte. Utiliser le nom générique sans article si possible",
        "parameters": {
          "type": "object",
          "properties": {
            "triples": {
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
          "required": ["triples"]
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
        function_call={"name": "extract_triples"}
    )

    triples = response.choices[0].message.function_call.arguments
    
    def dict_to_list(d:dict) -> list:
      result = [
        (t["subject"], t["predicate"], t["object"]) for t in d["triples"]
      ]
      return result

    entities = dict_to_list(triples)
    
    return entities


# Test Input
text = "Le Crime de l'Orient Express est un roman. Le roman a été écrit par Agatha Christie."
# text = "Le patient prend un médicament. Le médecin prescrit un traitement." 
# text = "Marie Curie a découvert le polonium."


# triples = {"triples":[{"subject":"Le Crime de l'Orient Express","predicate":"est","object":"un roman"},{"subject":"Le roman","predicate":"a été écrit par","object":"Agatha Christie"}]}
triples = {"triples":[{"subject":"Crime de l'Orient Express","predicate":"est","object":"roman"},{"subject":"roman","predicate":"a été écrit par","object":"Agatha Christie"}]}

print(triples)


