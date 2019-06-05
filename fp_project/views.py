from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from fp_project.forms import RegistrationForm


def register(request):
    '''
        input: an HTTP(S) request
        output: a rendered page
    '''
    template = 'registration/register.html'
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            user = authenticate(username=data['email'], password=data['password1'])
            if user is not None:
                login(request, user)
                return redirect('/')
    args = {'form': form}
    return render(request, template, args)
