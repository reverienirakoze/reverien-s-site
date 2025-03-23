from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def contact_view(request):
    return render(request, 'contact/contact.html')
