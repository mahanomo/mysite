from django.urls import path
from website import views

urlpatterns = [
    path("",views.index_view),
    path("contact/",views.contact_view),
    path("about/",views.about_view),
]