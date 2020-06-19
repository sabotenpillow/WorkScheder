from django import forms
from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserWorkPatternUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('workPattern', 'adjust_num',)
        #fields = ('username', 'password', 'workPattern_id', 'adjust_num',)

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    for field in self.fields.values():
    #        field.widget.attrs['class'] = 'form-control'
