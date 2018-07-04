from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    content = forms.TextInput()
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['content', 'image']

    def saves(self, author):
        return Post.objects.create(
            author = author,
            image = self.cleaned_data['image'],
            content= self.cleaned_data['content'],
        )