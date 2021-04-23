from django.shortcuts import render, redirect
from .models import Item
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', { 'items': items })

class ItemsCreate(CreateView):
    model = Item
    fields = '__all__'

def items_delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect('/')