from django.shortcuts import render


def index(response):
    return render(response, "kitchen/index.html")
