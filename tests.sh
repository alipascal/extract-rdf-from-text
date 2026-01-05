# EN

# short_sentences_astronomy
python main.py spacy --file "inputs\en\input_short_sentences_astronomy.txt" --lang en --output "output_spacy_short_sentences_astronomy_en"
python main.py openai --file "inputs\en\input_short_sentences_astronomy.txt" --lang en --output "output_openai_short_sentences_astronomy_en"
python main.py stanford --file "inputs\en\input_short_sentences_astronomy.txt" --lang en --output "output_stanford_short_sentences_astronomy_en"
python main.py nltk --file "inputs\en\input_short_sentences_astronomy.txt" --lang en --output "short_sentences_astronomy_en"
echo "short_sentences_astronomy finished"

# short_sentences
python main.py spacy --file "inputs\en\input_short_sentences.txt" --lang en --output "output_spacy_short_sentences_en"
python main.py openai --file "inputs\en\input_short_sentences.txt" --lang en --output "output_openai_short_sentences_en"
python main.py stanford --file "inputs\en\input_short_sentences.txt" --lang en --output "output_stanford_short_sentences_en"
python main.py nltk --file "inputs\en\input_short_sentences.txt" --lang en --output "output_nltk_short_sentences_en"
echo "short_sentences finished"

# wikipedia
python main.py stanford --file "inputs\en\input_wikipedia_astronomy_en.txt" --lang en --output "output_stanford_wikipedia_en"
python main.py spacy --file "inputs\en\input_wikipedia_astronomy_en.txt" --lang en --output "output_spacy_wikipedia_en"
python main.py openai --file "inputs\en\input_wikipedia_astronomy_en.txt" --lang en --output "output_openai_wikipedia_en"
python main.py nltk --file "inputs\en\input_wikipedia_astronomy_en.txt" --lang en --output "output_nltk_wikipedia_en"
echo "wikipedia finished"

# kaggle
python main.py spacy --file "inputs\en\input_articles_kaggle_dataset_kcovid_15.txt" --lang en --output "output_spacy_kaggle"
python main.py openai --file "inputs\en\input_articles_kaggle_dataset_kcovid_15.txt" --lang en --output "output_openai_kaggle"
python main.py stanford --file "inputs\en\input_articles_kaggle_dataset_kcovid_15.txt" --lang en --output "output_stanford_kaggle"
python main.py nltk --file "inputs\en\input_articles_kaggle_dataset_kcovid_15.txt" --lang en --output "output_nltk_kaggle"
echo "kaggle finished"


# FR

# short_sentences_astronomie_fr
python main.py spacy --file "inputs\fr\input_short_sentences_astronomie.txt" --lang en --output "output_spacy_short_sentences_astronomie_fr"
python main.py openai --file "inputs\fr\input_short_sentences_astronomie.txt" --lang en --output "output_openai_short_sentences_astronomie_fr"
echo "short_sentences_astronomie_fr finished"

# short_articles_fr
python main.py spacy --file "inputs\fr\input_articles_hal_medical.txt" --lang en --output "output_spacy_short_articles_fr"
python main.py openai --file "inputs\fr\input_articles_hal_medical.txt" --lang en --output "output_openai_short_articles_fr"
echo "short_articles_fr finished"

# wikipedia_fr
python main.py spacy --file "inputs\fr\input_wikipedia_astronomie_fr.txt" --lang en --output "output_spacy_wikipedia_fr"
python main.py openai --file "inputs\fr\input_wikipedia_astronomie_fr.txt" --lang en --output "output_openai_wikipedia_fr"
echo "wikipedia_fr finished"


# SEM WEB

# semweb_td_en
python main.py stanford --file "inputs\en\input_semweb_en_n1.txt" --lang en --output "output_stanford_semweb_td_en"
python main.py nltk --file "inputs\en\input_semweb_en_n1.txt" --lang en --output "output_nltk_semweb_td_en"

python main.py stanford --file "inputs\en\input_semweb_en_n2.txt" --lang en --output "output_stanford_semweb_td_en"
python main.py nltk --file "inputs\en\input_semweb_en_n2.txt" --lang en --output "output_nltk_semweb_td_en"

python main.py stanford --file "inputs\en\input_semweb_en_n3.txt" --lang en --output "output_stanford_semweb_td_en"
python main.py nltk --file "inputs\en\input_semweb_en_n3.txt" --lang en --output "output_nltk_semweb_td_en"
echo "semweb_td_en finished"

# semweb_td_fr
python main.py spacy --file "inputs\fr\input_semweb_fr_n1.txt" --lang en --output "output_spacy_semweb_td_fr_n1"
python main.py openai --file "inputs\fr\input_semweb_fr_n1.txt" --lang en --output "output_openai_semweb_td_fr_n1"

python main.py spacy --file "inputs\fr\input_semweb_fr_n2.txt" --lang en --output "output_spacy_semweb_td_fr_n2"
python main.py openai --file "inputs\fr\input_semweb_fr_n2.txt" --lang en --output "output_openai_semweb_td_fr_n2"

python main.py spacy --file "inputs\fr\input_semweb_fr_n3.txt" --lang en --output "output_spacy_semweb_td_fr_n3"
python main.py openai --file "inputs\fr\input_semweb_fr_n3.txt" --lang en --output "output_openai_semweb_td_fr_n3"
echo "semweb_td_fr finished"

