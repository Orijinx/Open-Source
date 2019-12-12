from django import forms


class qr_service(forms.Form):
    img_url = forms.CharField(max_length=200, label="URL изображения")
    qr_img = forms.FileField(required=False)

