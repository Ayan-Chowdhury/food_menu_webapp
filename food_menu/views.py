from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
# Create your views here.

def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render (request, 'food_menu/index.html',context)

def item(request):
    return HttpResponse('This is an item view')


def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        "item":item,
    }
    return render(request, 'food_menu/detail.html', context)


def create_item(request):
    form=ItemForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect('food_menu:index')

    
    return render(request, 'food_menu/item-form.html',context)

def update_item(request,id):
    item=Item.objects.get(id=id)
    
    form=ItemForm(request.POST or None, instance=item)
    context={
        'item':item,
        'form':form,
        
    }
    if form.is_valid():
        form.save()
        return redirect('food_menu:index')
    
    return render(request,'food_menu/item-form.html',context)