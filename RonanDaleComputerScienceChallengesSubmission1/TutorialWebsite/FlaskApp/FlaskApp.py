#FLASK IMPORTS
from flask import Flask, render_template, url_for,redirect, request
from Form import RegForm, LoginForm
from flaskext.markdown import Markdown
from flask import flash
#NLP IMPORTS
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
#SPACY FUNCTIONS
def get_ents(doc):
    res = []
    res += ([X.text,X.label_] for X in doc.ents)
    return len(res)
app = Flask(__name__,static_url_path='/static') #images will be taken from this folder.
Markdown(app)
app.config['SECRET_KEY'] = 'e2867020036883fc9b7f70ab302be773'

@app.route("/")
def index():
    return render_template('tutorial1.html')

@app.route("/tutorial1",methods=['GET', 'POST'])
def tutorial1():
    return render_template('tutorial1.html',title = 'Rule-Based Matching')

@app.route("/extract",methods=["GET","POST"])
def extract():   
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        doc = nlp(rawtext)
        render = displacy.render(doc,style='ent',options={'fine_grained': True})#ent is the render type for entities. dep is the render type for dependencies.
        count = get_ents(doc)
        result = render
    return render_template('results.html',result=result,rawtext=rawtext,count=count)

@app.route("/tutorial2")
def tutorial2():
    return render_template('tutorial2.html',title = 'Rule-Based Matching')
@app.route("/troubleshooting")
def troubleshooting():
    return render_template('troubleshooting.html',title='Troubleshooting')
if __name__ == '__main__':
    app.run(debug=True)
