from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

User = get_user_model()

class Author(models.Model):
    # OneToOneField used when one record of a model A is related to exactly one record of another model B,
    # in this case the get_user_model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username
        
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # auto_now_add field is saved as the current timestamp when a row is first added to the database
    # example: if the item being updated, the field won't be update.
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True, blank=True)
    featured = models.BooleanField()
    content = HTMLField()

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-date')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE) #Class Post

    def __str__(self):
        return self.user.username