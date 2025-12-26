import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')

def basic_stats(text):
    sents = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    avg_sent_len = np.mean([len(w.split()) for w in sents]) if sents else 0
    ttr = len(set(words)) / (len(words) + 1)
    punct_ratio = sum(1 for ch in text if ch in '!?.,;:') / (len(text) + 1)
    return [avg_sent_len, ttr, punct_ratio]

class Featurizer:
    def __init__(self, max_features=5000, ngram=(1,2)):
        self.tfidf = TfidfVectorizer(max_features=max_features, ngram_range=ngram)

    def fit(self, texts):
        self.tfidf.fit(texts)

    def transform(self, texts):
        Xtf = self.tfidf.transform(texts)
        basic = np.array([basic_stats(t) for t in texts])
        from scipy.sparse import hstack
        return hstack([Xtf, basic])

    def fit_transform(self, texts):
        self.fit(texts)
        return self.transform(texts)
