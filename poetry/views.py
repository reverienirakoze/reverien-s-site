from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def poetry_view(request):
    return render(request, 'poetry/poetry.html')
