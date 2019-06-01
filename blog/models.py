from django.db import models
from django.conf import settings 

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):

        return self.name
        

class Post(models.Model):

    #django will automatically generate forms when we write these codes
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=60) # null=True , blank=True, default='Random Title' #(null=True means: let the user input value; blank=True means the user can't leave the space balnk)
    body = models.TextField()
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    featured = models.BooleanField(default=False)
    #image = models.ImageField()

    def __str__(self):

        return "{} published on {}".format(self.title,self.published)

class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    writer = models.CharField(max_length=50, default=True, blank=True)
    email = models.EmailField(max_length=120)
    body = models.TextField()
    active = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True) 
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):

        return "{} published on {}".format(self.writer,self.published)
