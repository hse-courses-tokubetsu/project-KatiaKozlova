import argparse
from bm import IndexatorBM25
from embed import Embedder
from lemm import Lemmatizer

def similarity(query: str, model_type: str, n: int=10) -> list[str]:
    '''
    Returns top-n most high ranked jokes to cater current search query.
    :param query: the input search query
    :param model_type: the input indexer
    :param n: the quantity of jokes (default top-10)
    :return: top-n closest jokes to cater current search query
    '''
    corpus, texts = Lemmatizer.preprocess()
    if model_type == 'w2v' or model_type == 'nvc':
        indexator = Embedder(corpus, texts, model_type)
    elif model_type == 'bm25':
        indexator = IndexatorBM25(corpus, texts)
    else:
        raise ValueError('Embedder must be BM-25 (bm25), Word2Vec (w2v) or Navec (nvc)!')
    return indexator.get_top_n(query, n)

def main():
    parser = argparse.ArgumentParser(description='Searcher of the Russian jokes!')
    parser.add_argument('query', type=str, help='What do you remember about the joke (put underscores instead of spaces)?') 
    parser.add_argument('model_type', type=str, help='What type of model would you like: BM-25 (bm25), Word2Vec (w2v) or Navec (nvc)?')
    parser.add_argument('--top', type=int, default=10, help='How many jokes would you like (default: 10)')
    args = parser.parse_args()
    
    print('\n'.join(similarity(args.query, ' '.join(args.model_type.split('_')), args.top)))

if __name__ == "__main__":
    main()