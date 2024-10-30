from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Mavzutanasi

class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())    
    class Meta:
        model = Mavzutanasi
        fields = '__all__'