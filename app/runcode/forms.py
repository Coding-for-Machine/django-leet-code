from django import forms
from .models import Answer,  Problems
from django_ckeditor_5.widgets import CKEditor5Widget



class ProblemsForms(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

      class Meta:
          model = Problems
          fields = "__all__"
          widgets = {
              "body": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

    
