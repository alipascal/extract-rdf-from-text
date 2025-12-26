"""
Testing Function Calling avec OpenAI models
"""
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(OPENAI_API_KEY=OPENAI_API_KEY)

functions = [
  {
    "name": "extract_triples",
    "description": "Extraire des triplets (sujet, prédicat, objet) depuis un texte",
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

# Test Input
text = "Le Crime de l'Orient Express est un roman. Le roman a été écrit par Agatha Christie."
# text = "Le patient prend un médicament. Le médecin prescrit un traitement." 
# text = "Marie Curie a découvert le polonium."

response = client.chat.completions.create(
    model="gpt-4.1",
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
print(triples)

