from django import template
from blog.models import Post,Category,Comment
register = template.Library()

@register.simple_tag(name='c_view')
def c_view(pid):
    posts = Post.objects.get(id=pid)
    posts.counted_view += 1
    posts.save(update_fields=("counted_view",))
    return posts.counted_view

@register.simple_tag(name='comment_view')
def comment_view(pid):
    comments= Comment.objects.filter(approach=True)
    comments = comments.filter(post_id = pid)
    # comments = comments(Post.objects.get(id=pid))
    return len(comments)

@register.inclusion_tag("blog/blog-latest-post.html")
def latest_posts():
    posts = Post.objects.filter(status='True')[:3]
    return {'posts':posts}

@register.inclusion_tag("blog/blog-cat.html")
def postcat():
    posts = Post.objects.filter(status='True')
    categories = Category.objects.all()
    dicti = {}
    for cat in categories :
        dicti[cat] = posts.filter(category=cat).count()
        
    return {'dicti':dicti}

@register.filter(name='times') 
def times(number):
    return range(number)