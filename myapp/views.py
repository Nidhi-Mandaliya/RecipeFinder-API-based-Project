from http.client import responses

from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = requests.get("https://dummyjson.com/recipes")
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    response = url.json()
    data = response["recipes"]
    print(data)

    context = {
        "data":data,
        "tags":tags
    }

    return render(request,"index.html",context)

def databytags(request,tag):
    print(tag)
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]
    context = {
        "data":data,
        "tags": tags
    }
    return render(request,"index.html",context)

def mealtype(request,meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    print(response)
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]
    context = {
        "data": data,
        "tags": tags
    }
    return render(request,"index.html",context)

def search(request):
    userquery = request.POST.get("query")
    print(userquery)
    response = requests.get(f"https://dummyjson.com/recipes/search?q={userquery}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]
    context = {
        "data": data,
        "tags": tags
    }

    return render(request,"index.html",context)

def singlepage(request,id):
    print(id)
    response = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    context = {
        "data":response
    }
    return render(request,"recipes.html",context)