from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ImageForm, Attributes, Classify
from PIL import Image
import requests
from io import BytesIO

def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        browse = ImageForm(request.POST, request.FILES)
        attr = Attributes(request.POST)
        if browse.is_valid():
            browse.save()
            return redirect('select_attributes')
    else:
        browse = ImageForm()
        attr = Attributes()
    return render(request, 'web/index.html', {'browse': browse, 'attr': attr})


def select_attributes(request):
    if request.method == 'POST':
        attr = Attributes(request.POST)
        if attr.is_valid():
            return redirect('classify')
    else:
        attr = Attributes()
    return render(request, 'web/select.html', {'attr': attr})


def classify(request):
    if request.method == 'POST':
        clas = Classify(request.POST)
        if clas.is_valid():
            result = 10 # Example
            time = 3 # Example
            return render(request, 'web/result.html', {'result': result, 'time': time})
    else:
        clas = Classify()
    return render(request, 'web/classify.html', {'clas': clas})