from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    template = 'manual/index.html'
    return render(request, template)
