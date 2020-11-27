from django.shortcuts import render, get_object_or_404
from .models import Additem
# Create your views here.

def index(request):
    itemlist = Additem.objects.all()
    return render(request, 'add/index.html', {'itemlist': itemlist})

def detail(request, item_id):
    item = Additem.objects.get(pk=item_id)
    return render(request, 'add/detail.html', {'item': item})

def new_item(request):
    if request.method == 'POST':
        new_article = Additem.objects.create(
                itemname=request.POST['itemname'],
                price=request.POST['price'],
                )
    return render(request, 'add/new_item.html')

