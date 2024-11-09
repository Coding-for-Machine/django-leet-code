
from django import forms
from .models import Mavzutanasi
from django_ckeditor_5.widgets import CKEditor5Widget

class MavzutanasiForms(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

      class Meta:
          model = Mavzutanasi
          fields = "__all__"
          widgets = {
              "body": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }