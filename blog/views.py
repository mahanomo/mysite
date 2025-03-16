from django.shortcuts import render
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def single_view(request):
    return render(request, "blog/blog-single.html")

def test(request,pid):
    
    def get_object(self, queryset=None):
        item = self.get_object(queryset)
        item.counted_view()
        return item
    
    posts = Post.objects.get(id=pid)
    nume=get_object(posts)
    # posts.counted_view += 1
    context = {'posts':nume}
    return render(request, "test.html",context,)
