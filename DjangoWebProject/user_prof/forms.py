from django import forms
from django.core.exceptions import ValidationError
from feed.models import Articles
class PostForm(forms.ModelForm):
    class Meta:
        model = Articles
        field = [
            'article',
             'text'
        ]

# class CommentsForm(forms.Form):
#     class Meta:
#         model = Comments
#         fields=[
#             'comm'
#         ]