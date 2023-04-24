from django import forms 
from .models import BlogPost

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"
        exclude = ['author'] 