from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField(label='Upload Your Resume')
