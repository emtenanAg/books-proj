from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
from Model import model
import pandas as pd
my_model = load("./SavedModels/my_model.pkl")


def Recommendation(request):
    return render(request, 'recommendation.html')


def Result(request):
    if request.method == "POST":
        query = request.POST.get("query")
        genre_list = request.POST.getlist("genres")
        genre_dict = {}
        i = 0
        for el in genre_list:
            genre_dict[i] = el
            i = i + 1

    books = my_model.retrive(query, genre_dict)
    books = books.drop_duplicates(subset=["book_id"])
    books = books.tail(30).iloc[::-1]
    return render(request, "result.html", context={"books": books, "genre_dict": genre_dict, "query": query})
