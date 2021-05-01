from django.shortcuts import render, redirect
from .models import Content
from .forms import ContentForm
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request, 'breadcat/home.html')

def create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('detail')
    else:
        form = ContentForm()
    return render(request, 'breadcat/create.html', {'form': form})


def detail(request):
    posts = Content.objects.all()
    return render(request, 'breadcat/detail.html', {'post_list':posts})

def edit(request, index):
    post = get_object_or_404(Content,pk=index)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now
            post.save()
            return redirect('detail', index=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'edit.html', {'form': form})
