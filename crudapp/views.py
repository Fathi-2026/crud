from venv import create

from django.shortcuts import render, get_object_or_404, redirect
from .models import item, Item


# Create your views here.
# CRUD
# create
from django.shortcuts import render, redirect
from .models import Item  # Ensure you import your Item model

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)  # Corrected 'Item' reference
        return redirect('item_list')  # Redirect after successful creation

    return render(request, 'item_form.html')  # Render the form for GET requests
# read
def read_item(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})
# Update
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': item})
# delete
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': item})