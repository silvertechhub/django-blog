from django import forms
from django.forms import ModelForm
from .models import Blog, Category


input_classes= "w-full py-4 px-6 rounded-xl border"
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'article',
            'topic',
            'image'
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class': input_classes}),
            'article':forms.Textarea(attrs={'class': input_classes}),
        }
       
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ] 