from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("",views.blog_view, name="index"),
    path("single",views.single_view, name="single"),
    path("post-<int:pid>",views.test, name="test"),
]
