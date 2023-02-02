from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница!',
        'values': ['Hello', 'Hi', 'Goodbay'],
        'obj': {
            'car': 'BMW',
            'age': '30',
            'hobby': 'fishing'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')

#def catalog(request):
    #return HttpResponse("<h1>Каталог<h1>")