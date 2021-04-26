from django.shortcuts import render


# Create your views here.
# функции = контроллеры = вьюхи

def index(request):
    context = {'title', 'GeekShop'}
    return render(request, 'minapp/index.html', context)

def products(request):
    context = {'title', 'GeekShop - Каталог'}
    return render(request, 'minapp/products.html', context)


