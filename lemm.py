# lemm.py

import nltk
from nltk.corpus import stopwords
import pymorphy2
import string
import zipfile
import pandas as pd


class Lemmatizer():
    def __init__(self):
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)

        self.morph = pymorphy2.MorphAnalyzer()
        self.russian_stopwords = stopwords.words('russian')
      
    def lemmatization(self, sent: str) -> list[str]:
        '''
        This function lemmatizes one string.
        :param sent: one raw string
        :return: list of lemmatized words of the string
        '''
        lemmatized_string = []
        for word in nltk.word_tokenize(sent, language="russian"):
            lemma = self.morph.parse(word)[0].normal_form.strip(string.punctuation + '«—»')
            lemma = lemma.replace('ё', 'е')
            if lemma and lemma not in self.russian_stopwords and lemma not in (string.punctuation + '«—»') and lemma != '...':
                lemmatized_string.append(lemma)
        return lemmatized_string
    
    def sentences_lemmatization(self, sentences: list[str]) -> list[list[str]]:
        '''
        This function lemmatizes sentences.
        :param sentences: list of raw strings
        :return: list of senetences as a list of lemmatized words
        '''
        lemmatized_texts = []
        for sentence in sentences:
            lemmatized_text = self.lemmatization(sentence)
            lemmatized_texts.append(lemmatized_text)
        return lemmatized_texts
    
    def preprocess(self) -> tuple[list[list[str]], list[str]]:
        '''
        This function preprocess our zip-file.
        :return: corpus of jokes and preprocessed corpus
        '''
        with zipfile.ZipFile('jokes.zip', 'r') as archive:
            archive.extractall()
        df = pd.read_csv('jokes.csv')
        self.texts = list(set(df[df.rating >= 5].text.values.tolist()))
        self.corpus = self.sentences_lemmatization(self.texts)
        return self.corpus, self.texts