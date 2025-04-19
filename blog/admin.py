from django.contrib import admin
from blog.models import Post,Category,Comment
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author" ,"counted_view", "status", "published_date", "created_date"]
    list_filter = ["status","tags"]
    # ordering = ["-created_date"]
    search_fields = ["title","content"]
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'body', 'created_on', 'approach')
    list_filter = ('approach', 'created_on')
    search_fields = ('name', 'email', 'body')

admin.site.register(Category)