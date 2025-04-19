from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"
    domain = "127.0.0.1:8000"

    def items(self):
        return ["website:index", "website:about", "website:contact"]

    def location(self, item):
        return reverse(item)
