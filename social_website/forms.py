from django import forms
class SubtitleForm(forms.Form):
	language = forms.CharField(max_length = 100, label = 'language')
	subFile = forms.FileField(label = 'file')
