from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post,Comment
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    comments = Comment.objects.filter(post=post.id, approved=True)

    form = CommentForm()   # فرم همیشه تعریف می‌شود

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submit')

    posts = Post.objects.filter(status=1).order_by('created_date')
    posts_list = list(posts)

    current_index = posts_list.index(post)

    prev_post = None
    next_post = None

    if current_index > 0:
        prev_post = posts_list[current_index - 1]

    if current_index < len(posts_list) - 1:
        next_post = posts_list[current_index + 1]

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/blog-single.html', context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
    
    