from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

@login_required
def index(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect('/post')
    return render(request, 'post/index.html', {'all_posts': Post.objects.all(), 'form': form})
