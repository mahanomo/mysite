from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("",views.blog_view, name="index"),
    path("post-<int:pid>",views.single_view, name="single"),
    path("category/<str:cat_name>",views.blog_view, name="category"),
    path("tag/<str:tag_name>",views.blog_view, name="tags"),
    path("author/<str:author_username>",views.blog_view,name="author"),
    path("search/",views.blog_search,name="search"),
    path("test",views.test, name="test"),
]
