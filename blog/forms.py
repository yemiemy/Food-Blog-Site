from django import forms 
from .models import Comment, Post

class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('writer','email','body')

class postForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title','body','category')

	
	
		
