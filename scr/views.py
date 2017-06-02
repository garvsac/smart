from django.http import HttpResponse
from django.shortcuts import render
from scr.models import Category, quote
from django.views.generic import FormView
from scr.forms import MyModelForm, Quotation

def index(request):
    context_dict = {'boldmessage': "Scrap Management"}

    return render(request, 'scr/index.html', context=context_dict)

def add(request):
    form = MyModelForm()

    if request.method == 'POST':
        form = MyModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print(form.errors)

    return render(request, 'scr/add.html', {'form': form})
	
def quotes(request):
    form = Quotation()

    if request.method == 'POST':
        form = Quotation(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print(form.errors)

    return render(request, 'scr/quote.html', {'form': form})
