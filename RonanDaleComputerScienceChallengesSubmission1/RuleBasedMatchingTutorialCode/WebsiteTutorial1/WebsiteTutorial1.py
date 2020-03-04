#Libaries
import spacy
from spacy import displacy
from spacy.pipeline import EntityRecognizer
from spacy.matcher import Matcher
from spacy.lemmatizer import Lemmatizer
#Vocab creation
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
#Target body of text
text = ["The good player knows how to bluff. The better player knows how to tell when their opponent is bluffing. The best player knows how to make it seem like they’re bluffing when they’re not.",
        "This soldier shoots to kill. He spent all night shooting at the enemy soldiers and even shot at their general.",
        "Who was cutting the grass earlier? I thought the man with those large cuts on his leg wasn’t able to walk properly."]
#Patterns for each example
pattern1 = [{"LEMMA":"good"}]
pattern2 = [{"LEMMA":"shoot"}]
pattern3a = [{"LEMMA":"cut"}]
pattern3b = [{"LEMMA":"cut"},{"POS":"VERB"}]

question1 = [{"IS_TITLE":True},{"IS_ALPHA":True},{"IS_ALPHA":True},{"LIKE_EMAIL":True}]
question2 = [{"LOWER": "this"},{"POS":"VERB"},{"POS":"ADJ"}]
question3 = [{"IS_TITLE":True,"POS":""}]
#Method to call displaCy for text with multiple sentences
def displaCy(doc, bg_col, txt_col):
    sentence_spans = list(doc.sents)
    options = {"compact": True, "bg": bg_col,
           "color": txt_col, "font": "Georgia Pro"}
    displacy.serve(sentence_spans, style = "dep",options = options, port = 5001)
#Matcher method
def check_for_matches(target_text, pattern,match_tag):
    results = []
    matcher.add(match_tag,None,pattern)
    print(target_text)
    doc = nlp(target_text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        res = match_id,string_id,start,end,span.text
        results += res
    if len(results) > 0:
        displaCy(doc,"darkgreen","white")
        return results
    else:
       return "NO RESULTS."
#ask_question prompts the user to enter an expression which contains a phrase that satisfies the rule displayed.
def ask_question(question, pattern, match_tag):
    print(question)
    for token in pattern:
        print(token)
    answer = input()
    for match in check_for_matches(answer, pattern, match_tag):
        print(match)
#Main Code
question = "Enter an expression which satisfies the following rule:"
for match in check_for_matches(text[0],pattern1,"GOOD"):
    print(match)
for match in check_for_matches(text[1],pattern2,"SHOOT"):
    print(match)
ask_question(question,question1,"EMAIL STATEMENT")
ask_question(question,question2,"THIS *VERB* *ADJECTIVE*")
