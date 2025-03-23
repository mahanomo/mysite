from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag
def c_view(pid):
    posts = Post.objects.get(id=pid)
    posts.counted_view += 1
    posts.save(update_fields=("counted_view",))
    return posts.counted_view

@register.inclusion_tag("blog/blog-latest-post.html")
def latest_posts():
    posts = Post.objects.filter(status='True')[:3]
    return {'posts':posts}

