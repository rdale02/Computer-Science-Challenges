import spacy
import nltk
from spacy import tokenizer, lemmatizer, parts_of_speech
from spacy.matcher import Matcher
from nltk import wordnet
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
sentences = ["Bring my money to the bank.","Did you hear about what happened at the river bank?"
             "Bow down to your master.", "An arrow was shot from the bow"]
doc = nlp("Who shot this man?")
print(" ".join(token.lemma_ for token in doc))
matcher = Matcher(nlp.vocab)