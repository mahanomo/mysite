from blog.models import Post,Category
from django import template
register = template.Library()

@register.inclusion_tag("website/index.html")
def latest_post():
    posts = Post.objects.filter(status=1)
    context= {'posts':posts}
    print(context)
    return context