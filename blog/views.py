from django.shortcuts import render
from blog.models import Post
from next_prev import next_in_order, prev_in_order

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def single_view(request,pid):
    
    posts = Post.objects.get(id=pid,status=1)
    context= {"posts": posts }
    return render(request, "blog/blog-single.html",context)

def test(request,pid):
    
    posts = Post.objects.get(id=pid)
    posts.counted_view += 1
    posts.save(update_fields=("counted_view",))
    context = {'posts':posts}
    return render(request, "test.html",context,)
