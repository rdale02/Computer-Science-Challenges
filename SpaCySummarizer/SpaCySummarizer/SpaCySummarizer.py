#Streamlit
import streamlit
#Seaborn
import seaborn
#Gensim
from gensim.summarization import summarize as gensim_summariser
#Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
#SpaCy
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
#HTML
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
#Sumy Summariser
def sumy_summarise(text):
    parser = PlaintextParser.from_string(text,Tokenizer("english")) #formats sentences
    summariser = LexRankSummarizer() #see learning log for an explanation of Lexical Ranking
    summary_list = [str(sentence) for sentence in summariser(parser.document,6)]#list function 
    return ' '.join(summary_list)
#Visualiser
def visualise(sentences, ranker):
    x = 0;
    while x < len(sentences) 
#Main Body
def main():
    streamlit.title("Summariser and NER Tool")
    options = streamlit.sidebar.selectbox("Select an Option",["Summarise","Entity Recognition"])
    if options == "Summarise":
        streamlit.subheader("Summariser")
        input = streamlit.text_area("Summarise Text")
        summariser_choice = streamlit.selectbox("Summarise with",["Sumy","Gensim"])	
        if streamlit.button("Summarise"):	
            if summariser_choice == "Gensim":
                result = gensim_summariser(input)
            if summariser_choice == "Sumy":
                result = sumy_summarise(input)
            streamlit.write(result)
    if options == "Entity Recognition":
        streamlit.subheader("SpaCy Recognition")
        input = streamlit.text_area("Check for Entities")
        if streamlit.button("Run"):
            doc = nlp(input)
            html = displacy.render(doc,style="ent")#Displacy will show all entities from the doc which are in the pre-trained vocabulary.
            html = html.replace("\n\n","\n")
            streamlit.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
if __name__ == '__main__':
    main()