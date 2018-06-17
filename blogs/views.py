from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def list_blogs(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'blogs.html', {'blogs': blogs})


def create_blog(request):
    form = BlogForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_blogs')

    return render(request, 'blogs-form.html', {'form': form})


def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('list_blogs')

    return render(request, 'blogs-form.html', {'form': form, 'blog': blog})


def delete_blog(request, id):
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect('list_blogs')

    return render(request, 'blogs-delete-confirm.html', {'blog': blog})

