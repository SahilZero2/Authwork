from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'slug' , 'content' , 'thumbnail', 'author', )

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'thumbnail' : forms.ImageField( required=True),
            # 'profile' : forms.TextInput(attrs={'class': 'form-control', 'value' : '', 'id':'profile', }),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value' : '', 'id':'author', 'type':'hidden'}),

        }
