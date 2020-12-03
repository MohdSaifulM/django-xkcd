from django.shortcuts import render
import requests
import random

# Create your views here.

def index(request):
    URL = 'http://xkcd.com/info.0.json'
    #get latest comic
    data = requests.get(URL).json()
    #take lastest updated comic
    latest_updated = data['num']
    #randomize using latest_updated
    n = random.randint(1, latest_updated)
    
    if request.method == "POST":
        random_URL = 'http://xkcd.com/{}/info.0.json'.format(n)

        data = requests.get(random_URL).json()

    return render(request, 'index.html', {"data": data})