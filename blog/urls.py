from django.urls import path

from blog import views
app_name="blog"


urlpatterns = [
    path("",views.list,name="index"),
    path('list/',views.list,name="list"),
    path("create/",views.create,name="create"),
    path("edit/<int:blog_id>/",views.edit,name="edit"),
    path("delete/<int:blog_id>/",views.delete,name="delete"),
]