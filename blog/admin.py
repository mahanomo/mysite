from django.contrib import admin
from blog.models import Post,Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author" ,"counted_view", "status", "published_date", "created_date"]
    list_filter = ["status"]
    # ordering = ["-created_date"]
    search_fields = ["title","content"]
        
admin.site.register(Category)