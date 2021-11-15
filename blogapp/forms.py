from django import forms

class BlogForm(forms.Form):
    #입력 받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)