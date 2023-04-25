"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.shortcuts import HttpResponse,render

#view function
def index(request):
    return HttpResponse("OK THIS IS A HTTP RESPONSE")

def myname_view(request,name):

    return HttpResponse("MY NAME IS {}".format(name))

def multiply_view(reqeust,num1,num2):
    result = num1 * num2
    return HttpResponse("Result is {}".format(result))




def form_view(request):
    print(request.GET)
    name = request.GET.get('name')
    address = request.GET.get('address')

    return HttpResponse("FORM dATA is {} {}".format(name,address) )


def index_render(request):

    context = {

    }

    return render(request,"index.html",context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("myname/<str:name>/",myname_view,name="myname_view"),
    path("mul/<int:num1>/<int:num2>/",multiply_view,name="multiply_view"),
    path("form/",form_view,name="form_view"),
    path("blog/",include('blog.urls'))
]
