from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from datetime import datetime
from .forms import BlogCreateForm
from .models import BlogPost
# Create your views here.
def list(request):
    blogs = BlogPost.objects.all()
    data = {
        "blogs":blogs
    }

    # data = {
    #    "blogs": [{
    #     "title":"Titanic A Wonderful Ship",
    #     "date":datetime.now(),
    #     "author":"Aarav Poudel"
    #    },{
    #     "title":"Is Yatri really closed?",
    #     "date":datetime.now(),
    #     "author":"Shyam Sharma"
    #    }] 
    # }
    return render(request,"blog/list.html",data)

def create(request):
    form = BlogCreateForm()
  
    if request.method == "POST":
        form = BlogCreateForm(request.POST or None)
        if form.is_valid():
            blog = form.save(commit=False)
            # blog.date = timezone.now()
            blog.save()
            return redirect("blog:list")
        
    data  = {
        "form":form
    }
    return render(request,'blog/create.html',data)

def edit(request,blog_id):
    blog = get_object_or_404(BlogPost,id=blog_id)
    form = BlogCreateForm(instance=blog)

    if request.method == "POST":
        form = BlogCreateForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog:list")
    data = {
        "blog":blog,
        "form":form
    }
    return render(request,"blog/edit.html",data)


def delete(request,blog_id):
    blog = get_object_or_404(BlogPost,id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect("blog:list")
    data = {
        "blog":blog
    }
    return render(request,'blog/delete.html',data)

from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect("blog:index")
        else:
            messages.error(request,"Username or Password error")


    return render(request,'login.html',{})