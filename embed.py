#embed.py

from typing import Any
import numpy.typing as npt
import numpy as np
from navec import Navec
import zipfile
import gensim
from sklearn.metrics.pairwise import cosine_similarity
from lemm import Lemmatizer


class Embedder():
    def __init__(self, corpus: list[list[str]], texts: list[str], model_type: str):
        '''
        :param corpus: the input tokenized corpus
        :param texts: the input corpus
        :param model_type: type of model (Word2Vec (w2v) or Navec (nvc))
        '''
        self.lemmatizer = Lemmatizer()
        self.corpus = corpus
        self.texts = texts
        self.indexes = []
        if model_type == 'nvc':  #navec model https://github.com/natasha/navec
            # the link: https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar
            path_to_model = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
            self.model = Navec.load(path_to_model)
        else:
            # the link: http://vectors.nlpl.eu/repository/20/65.zip
            path_to_model = '65.zip'
            with zipfile.ZipFile(path_to_model, 'r') as archive:
                archive.extract('model.bin', '.')
            self.model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)
            

    def sent2vec(self, sentence: list[str]) -> npt.NDArray[np.float32]:
        '''
        This function gets vector for the sentence.
        :param sentences: list of raw strings
        :param model: model of vectorization
        :return: numpy array of embeddings of type float32
        '''
        vecs = []
        for word in sentence:
            try:
                vecs.append(self.model[word])
            except:
                pass
        return np.mean(np.array(vecs), axis=0)

    def get_vectors(self):
        for sentence in self.corpus:
            self.indexes.append(self.sent2vec(sentence))
    
    def get_top_n(self, query: str, n: int=10) -> list[str]:
        '''
        Prints top-n most high ranked jokes to cater current search query.
        :param query: the input search query
        :param n: the quantity of jokes (default top-10)
        :return: top-n closest jokes to cater current search query
        '''
        if not self.indexes:
            self.get_vectors()
        query2vec = self.sent2vec(self.lemmatizer.lemmatization(query)).T
        similarity = []
        for vecs in self.indexes:
            similarity.append(cosine_similarity(vecs.reshape(1, -1), query2vec.reshape(1, -1)))
        sorted_similarity = sorted(enumerate(similarity), key=lambda x: x[1], reverse=True)
        top_n = [f'{str(i + 1)}.\n{self.texts[pair[0]]}\n' for i, pair in enumerate(sorted_similarity[:n])]
        return top_n