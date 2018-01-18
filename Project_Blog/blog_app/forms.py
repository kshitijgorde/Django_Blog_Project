from django import forms
from blog_app.models import Comment, Post

class PostForm(forms.ModelForm):
    ''' Class for filling up the Blog post related attributes '''


    class Meta():
        model = Post
        fields = ('author', 'title', 'text') # Only these are to be filled up!

        widgets = {
        'title':forms.TextInput(attrs=
        {'class':'textinputclass'}
        ),
        'text': forms.Textarea(attrs = {
        'class' : 'editable medium-editor-textarea postcontent'
        })}

class CommentForm(models.ModelForm):
    ''' Form Class for comment inputs '''

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
        'author':forms.TextInput(attrs=
                                {'class':'textinputclass'}),
        'text': forms.Textarea(attrs =
                                {'class' : 'editable medium-editor-textarea'}),
        }
