from django import forms
from apps.movies.models import Movies


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    emial = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)