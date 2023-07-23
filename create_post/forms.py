from home.models import Post
from django.contrib.auth.models import User
from django import forms


class PostForm(forms.ModelForm):

    # Define initial values for form fields
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['category'].required = True

    class Meta:

        # Define model being used
        model = Post

        # Define model fields to be altered
        fields = (
            'title', 'category',
            'excerpt', 'content',
        )

        # Style and input definition
        widgets = {

            'title': forms.TextInput(
                attrs={
                    'style': 'width: 360px; max-width: 90%;',
                    'class': 'mb-2',
                }),

            'content': forms.Textarea(
                attrs={
                    'style': 'width: 100%',
                    'cols': 100, 'rows': 10,
                    'class': 'mb-2',
                }),

            'excerpt': forms.Textarea(
                attrs={
                    'cols': 120, 'rows': 6,
                    'class': 'mb-2 d-block m-0 w-100',
                }),

            'category': forms.Select(
                attrs={
                    'style': 'width: 189px; height: 30px',
                    'class': 'mb-3',
                }),
        }

        # Custom labels
        labels = {
            'title': 'Choose your Title',
        }
