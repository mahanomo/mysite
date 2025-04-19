from django.contrib import admin
from website.models import Contact,Newsletter
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]
    list_filter = ["email"]
    # ordering = ["-created_date"]
    search_fields = ["name","message"]

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email"]