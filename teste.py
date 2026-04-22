import spacy

nlp = spacy.load("pt_core_news_lg")
doc = nlp("João Silva esteve em Brasília no dia 10/03/2023.")

for ent in doc.ents:
    print(ent.text, ent.label_)