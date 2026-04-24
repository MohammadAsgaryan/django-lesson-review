from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
    posts = Post.objects.filter(status=1).order_by('created_date')
    posts_list = list(posts)
    current_index = posts_list.index(post)
    prev_post = None
    next_post = None
    if current_index > 0:
        prev_post = posts_list[current_index - 1]

    # اگر پست بعدی وجود دارد
    if current_index < len(posts_list) - 1:
        next_post = posts_list[current_index + 1]
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-single.html',context)
