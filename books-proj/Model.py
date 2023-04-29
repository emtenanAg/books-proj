import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class model:

    def __init__(self, reviews, tfidf_wm, tfidf_tokens):
        self.reviews = reviews
        self.tfidf_wm = tfidf_wm
        self.tfidf_tokens = tfidf_tokens

    def retrive(self, query, tags):
        # Instead of using fit_transform, you need to first fit
        # the new document to the TFIDF matrix corpus like this:
        queryTFIDF = TfidfVectorizer().fit(self.tfidf_tokens)
        # Now we can 'transform' this vector into that matrix shape by using the transform function:
        queryTFIDF = queryTFIDF.transform([query])
        # As we transformed our query in a tfidf object
        # we can calculate the cosine similarity in comparison with
        # our pevious corpora
        cosine_similarities = cosine_similarity(
            queryTFIDF, self.tfidf_wm).flatten()
        # Get most similar jobs based on next text
        related_product_indices = cosine_similarities.argsort()[:-500:-1]
        all_books = self.reviews.iloc[related_product_indices]
        all_books = all_books[all_books["genres"].apply(
            lambda x: any(k in tags.values() for k in x.keys()))]
        my_books_indecies = all_books["average_rating"].argsort()
        my_books = all_books.iloc[my_books_indecies]

        return my_books
