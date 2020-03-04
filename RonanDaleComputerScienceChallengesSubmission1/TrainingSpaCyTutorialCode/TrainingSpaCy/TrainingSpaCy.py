#REQUIRED LIBRARIES
import random
from pathlib import Path
import spacy
from tqdm import tqdm
#USES ENGLISH SPACY
nlp = spacy.load('en_core_web_sm')
#TRAINING_DATA //TRAINS FOR 'RONAN' AND 'DERRY' (SPACY DOESN'T IDENTIFY THESE CORRECTLY) AND 'RONAN DALE' WHICH IT DOES.
training_data = [
    ("Who was Ronan Dale?",{'entities':[(8,18,'PERSON')]}),
    ("Ronan is the best tennis player in Derry.",{'entities':[(0,5,'PERSON'),(35,40,'GPE')]}),
    ("Derry's best tennis player is called Ronan.",{'entities':[(0,5,'GPE'),(37,42,'PERSON')]}),
    ("Rafa invited Ronan to Derry's biggest tennis tournament.",{'entities':[(0,4,'PERSON'),(13,18,'PERSON'),(22,27,'LOC')]}),
    ("Where was Ronan Dale?",{'entities':[(10,20,'PERSON')]}),
    ("I think Ronan went to collect his lottery prize.",{'entities':[(8,13,'PERSON')]}),
    ("What cars does Ronan drive?",{'entities':[(15,20,'PERSON')]}),
    ("I saw Ronan driving a Tesla around Derry!",{'entities':[(6,11,'PERSON'),(22,27,'PRODUCT'),(30,35,'GPE')]}),
    ("How could Ronan afford a Tesla?",{'entities':[(10,15,'PERSON'),(25,30,'PRODUCT')]}),
    ("Did you know that Ronan works for PWC?",{'entities':[(18,23,'PERSON')]}),
    ("Wow!",{'entities':[]}),
    ("Do they have an office in Derry?",{'entities':[(26,31,'GPE')]}),
    ]
testing_data = [
    ("Do you know Ronan Dale?",{'entities':[(7,17,'PERSON')]}),
    ("Ronan is the worst tennis player in Derry.",{'entities':[(0,5,'PERSON'),(35,40,'GPE')]}),
    ("Derry's worst tennis player is called Ronan.",{'entities':[(0,5,'GPE'),(37,42,'PERSON')]}),
    ("Nobody invited Ronan to Derry's biggest tennis tournament.",{'entities':[(15,20,'PERSON'),(24,29,'LOC')]}),
    ("Where is Ronan Dale?",{'entities':[(9,19,'PERSON')]}),
    ("I don't think Ronan wants to collect his lottery prize.",{'entities':[(14,19,'PERSON')]}),
    ("What car did Ronan drive?",{'entities':[(13,18,'PERSON')]}),
    ("I saw Ronan driving a Tesla!",{'entities':[(6,11,'PERSON'),(22,27,'PRODUCT')]}),
    ("How can Ronan afford a Tesla?",{'entities':[(8,13,'PERSON'),(23,28,'PRODUCT')]}),
    ("Don't you know that Ronan works for PWC?",{'entities':[(20,25,'PERSON'),(36,39,'ORG')]}),
    ("Really?",{'entities':[]}),
    ("Do they have an office in Derry?",{'entities':[(26,31,'GPE')]}),
    ]
def train_ner(model = None, output_dir=Path("C:\\Users\rjdpo\\ronancode"),n_iter=100):
  nlp = load(model)
  ner = get_ner(nlp)
  losses = train(training_data,ner,n_iter)
  test(training_data)
  save()

def load(model):
    if model is not None:
        spc = spacy.load(model)  # load existing SpaCy model
        print("Loaded model '%s'" % model)
        return spc
    else:
        spc = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
        return spc
def get_ner(nlp):
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe('ner')
    return ner

def train(training_data,ner,n_iter):
    for _, annotations in training_data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(training_data)#Randomises the order of the training data
            losses = {}
            for text, annotations in tqdm(training_data):
                nlp.update([text],  # batch of texts
                    [annotations],# batch of annotations
                    drop=0.3,  # dropout makes it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            return losses

def test(data):#Uses your model on the training data.
    for text, _ in data:
        doc = nlp(text)
        print('Entities:', [(ent.text, ent.label_) for ent in doc.ents])

def save():
    nlp.to_disk("C:\\Users\\rjdpo\\ronancode")

def test_saved(output_dir,data):#COMPARE RESULTS BETWEEN RONANCODE AND SPACY
    print("Loading from", output_dir)
    nlp2 = spacy.load(output_dir)#Loads your model
    for text, _ in data:
        doc = nlp2(text)#processes text data
        print('Entities:', [(ent.text, ent.label_) for ent in doc.ents])
    print("Loading from SpaCy")
    nlp = spacy.load('en_core_web_sm')
    test(data)

train_ner()
test_saved("C:\\Users\\rjdpo\\ronancode",testing_data)