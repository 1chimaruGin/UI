import pandas as pd 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import csvForm

def index(request):
    if request.method == 'POST':
        browse = csvForm(request.POST, request.FILES)
        if browse.is_valid():
            obj = browse.save()
            csv_data = pd.read_csv(obj.csv.path)
            column = [name for name in csv_data.columns]
            data = csv_data.head().values.tolist()
            return render(request, 'web/select.html', {'browse': browse, 'column': column, 'data': data})
    else:
        browse = csvForm()
    return render(request, 'web/index.html', {'browse': browse})

def select(request):
    column = ['battery_power', 'int_memory', 'ram', 'four_g', 'sc_h', 'sc_w', 'talk_time']
    return render(request, 'web/pearson.html', {'column': column})

def classify(request):
    result = 10 # Example
    time = 3 # Example
    return render(request, 'web/result.html', {'result': result, 'time': time})