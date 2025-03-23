from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def interests_view(request):
    return render(request, 'interests/interests.html')
