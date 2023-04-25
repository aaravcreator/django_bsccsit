from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Person

def blog_index(request):
    persons = Person.objects.all()
    print(Person.objects.all().query)
    data = {
        "blogs":persons,
        "single":"this is single one"
    }
    return render(request,"blog/index.html",data)

from .forms import PersonForm
def blog_create(request):
    form = PersonForm()

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_index")
    data = {
        "form":form,
    }
    return render(request,"blog/create.html",data)

def edit(request,person_id):
    person = Person.objects.get(id=person_id)

    form = PersonForm(instance=person)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_index")
    data = {
        'form':form,
        'person':person
    }
    return render(request,"blog/edit.html",data)


def delete(request,person_id):
    # we use get object or 404 to give 404 error if person doesn't exist
    person = get_object_or_404(Person,id=person_id)

    if request.method == "POST":
        # we know its for delete
        person.delete()
        return redirect("blog:blog_index")
    data = {
        'person':person
    }
    return render(request,'blog/delete.html',data)
