from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tool
from .forms import ToolForm

@login_required
def index(request):
    form = ToolForm()
    if request.method == 'POST':
        form = ToolForm(request.POST)
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect('/tool')
    return render(request, 'tool/index.html', {'all_tools': Tool.objects.all(), 'form': form})
