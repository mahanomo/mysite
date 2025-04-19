from django.urls import path
from website import views
app_name = "website"

urlpatterns = [
    path("",views.index_view, name="index"),
    path("contact/",views.contact_view, name="contact"),
    path("about/",views.about_view, name="about"),
    path("newsletter/",views.Newsletter_view,name="newsletter"),
]