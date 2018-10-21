from django import forms
from .models import Post

class PostFormulario(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titulo','texto')
		widgets = {
			'texto': forms.TextInput(attrs={'class': 'materialize-textarea'}),
		}