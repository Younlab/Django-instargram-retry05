from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'uk-textarea'
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput()
    )
    class Meta:
        model = Post
        fields = ['content', 'image']

    def saves(self, author):
        return Post.objects.create(
            author = author,
            image = self.cleaned_data['image'],
            content= self.cleaned_data['content'],
        )