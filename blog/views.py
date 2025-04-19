from django.shortcuts import render,HttpResponseRedirect
from blog.models import Post,Comment
from next_prev import next_in_order, prev_in_order
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from blog.form import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name = kwargs['tag_name']) 
    paginator = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        posts = paginator.get_page(page_number=1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        posts = paginator.get_page(page_number=1)
    
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

@login_required
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
    
    comments= Comment.objects.filter(approach=True)
    comments = comments.filter(post_id = pid)
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Form submitted successfully.')
            return HttpResponseRedirect(f"post-{posts.id}")
        # else:
        #     messages.add_message(request, messages.ERROR, 'Captcha incorrect!')
        #     return HttpResponseRedirect("blog/blog-single.html")
    else:
        form = CommentForm()
    
    context['comments'] = comments
    context['form'] = form
    return render(request, "blog/blog-single.html",context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    query = request.GET.get("q")
    posts = posts.filter(Q(content__contains=query))
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def test(request):
    return render(request, "test.html")
