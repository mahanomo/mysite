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
    navigator = Post.objects.values_list('id')
    listi = []
    ind = 0
    counter = 0
    for i in navigator:
        listi.append(i[0])
        if pid == i[0]:
            ind = counter
        counter+=1
    if ind+1 > len(listi)-1:
        perv = listi[ind-1]
        context= {"posts": posts,"next":None,"perv":perv }
    elif ind-1 < 0 :
        next = listi[ind+1]
        context= {"posts": posts,"next":next,"perv":None }
    else:
        next = listi[ind+1]
        perv = listi[ind-1]
        context= {"posts": posts,"next":next,"perv":perv }
    return render(request, "blog/blog-single.html",context)


def test(request):
    return render(request, "test.html")
