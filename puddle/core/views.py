from django.shortcuts import render

from Item.models import Item, Category


#importando os itens

# Criado a primeira requisição view


def index(request):
    item=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'items':item
    })
def contact(request):
    return render(request,'core/contact.html')