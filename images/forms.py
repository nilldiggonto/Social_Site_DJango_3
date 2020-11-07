from django import forms
from .models import Image

#
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','url','description',]
        
    
    def clean_url(self):
        url                 = self.cleaned_data['url']
        valid_extensions    = ['jpg','jpeg','png']
        extension           = url.rsplit('.',1)[1].lower()

        if extension not in valid_extensions:
            raise forms.ValidationError('Something went wrong with the url')
        return url

    def save(self,force_insert=False,force_update=False,commit=True):
        images           = super().save(commit=False)
        image_url       = self.cleaned_data['url']
        name            = slugify(images.title)
        extension       = image_url.rsplit('.',1)[1].lower()
        image_name      = f'{name}.{extension}'

        #download image
        response        = request.urlopen(image_url)
        images.images.save(image_name,ContentFile(response.read()), save=False)

        if commit:
            images.save()
        return images