import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def text_to_sentences(text):
    sentences = sent_tokenize(text)
    return sentences
