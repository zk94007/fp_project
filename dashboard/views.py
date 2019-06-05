from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    if (request.user.is_authenticated):
        return redirect('post/')
    template = 'dashboard/index.html'
    return render(request, template)
