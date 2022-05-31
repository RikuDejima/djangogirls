from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class CureateAccount(forms.Form):
    id = forms.CharField()
    password = forms.CharField()
    mail = forms.EmailField(label="メールアドレス") 