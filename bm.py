# bm.py

from rank_bm25 import BM25Okapi as BM25
import numpy as np
import numpy.typing as npt
from lemm import Lemmatizer


class IndexatorBM25():
    def __init__(self, corpus: list[list[str]], texts: list[str]):
        self.lemmatizer = Lemmatizer()
        self.corpus = corpus
        self.texts = texts
        self.bm25 = BM25(self.corpus)
        self.vocab = []
        self.indexes = []
        
    def get_indexes(self):
        '''
        This function gets indexes with BM-25.
        '''
        for joke in self.corpus:
            for word in joke:
                if word not in self.vocab:
                    self.vocab.append(word)
        bm25_indexes = np.zeros((len(self.vocab), len(self.corpus)))
        for i, word in enumerate(self.vocab):
            bm25_indexes[i] = self.bm25.get_scores([word])
        self.indexes = bm25_indexes
    
    def get_top_n(self, query: str, n: int=10) -> list[str]:
        '''
        Prints top-n most high ranked jokes to cater current search query.
        :param query: the input search query
        :param n: the quantity of jokes (default top-10)
        :return: top-n closest jokes to cater current search query
        '''
        if isinstance(self.indexes, list):
            self.get_indexes()
        tokenized_query = self.lemmatizer.lemmatization(query)
        similarity = np.zeros((len(self.corpus)))
        for word in tokenized_query:
            if word in self.vocab:
                similarity += self.indexes[self.vocab.index(word)]
        sorted_similarity = sorted(enumerate(similarity.tolist()), key=lambda x: x[1], reverse=True)
        top_n = [f'{str(i + 1)}.\n{self.texts[pair[0]]}\n' for i, pair in enumerate(sorted_similarity[:n])]
        return top_n