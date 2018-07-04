from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm

def post_list(request):
    post = Post.objects.all()

    context = {
        'posts':post,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post-list')

    context = {
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)