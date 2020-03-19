#IMPORTS
import numpy as np
import nltk
from textblob import TextBlob
import matplotlib as mpt
import matplotlib.pyplot as plt
#DATASOURCE
data = {'A':"Star Wars is the best film ever made.",
        'B':"I didn't really like Star Wars.",
        'C':"Star Wars was too long and it got really boring.",
        'D':"Star Wars has some fascinating characters and beautiful planets.",
        'E':"Star Wars usually outperforms other franchises in the Box Office.",
        'F':"The most recent Star Wars film made me fall asleep.",
        'G':"Since they changed the director, Star Wars keeps getting better.",
        'H':"I love Star Wars!"}
#PLOTTER
for key in data.keys():
    x = TextBlob(data.get(key)).sentiment.polarity
    y = TextBlob(data.get(key)).sentiment.subjectivity
    plt.annotate(key,(x,y))
    plt.scatter(x,y)
#LABELS
plt.xlabel("Subjectivity")
plt.ylabel("Polarity")
#SHOW GRAPH
plt.show()
