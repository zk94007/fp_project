from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Game
from .forms import GameForm

@login_required
def index(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect('/game')
    return render(request, 'game/index.html', {'all_games': Game.objects.all(), 'form': form})
