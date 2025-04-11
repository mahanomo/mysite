from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("",views.blog_view, name="index"),
    path("post-<int:pid>",views.single_view, name="single"),
    # path("category/<str:cat_name>",views.blog_category, name="category"),
    path("test",views.test, name="test"),
]
