from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def resume_view(request):
    return render(request, 'resume/resume.html')
