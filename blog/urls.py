from django.urls import path



app_name= "blog"
from .views import *
urlpatterns = [
    path("", blog_index,name="blog_index"),
    path("create/",blog_create,name="blog_create"),
    path("edit/<int:person_id>/",edit,name="edit_view"),
    path("delete/<int:person_id>/",delete,name="delete_view"),
]