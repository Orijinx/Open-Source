from django import forms


class add_post(forms.Form):
    img_url = forms.CharField(max_length=200, label="URL изображения")
    title = forms.CharField(max_length=100, label='Название')
    about = forms.CharField(max_length=200, label='Описание')
    tag = forms.CharField(max_length=50,label='Хэштег')
