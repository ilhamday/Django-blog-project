from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Author(models.Model):
    # OneToOneField used when one record of a model A is related to exactly one record of another model B,
    # in this case the get_user_model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # auto_now_add field is saved as the current timestamp when a row is first added to the database
    # example: if the item being updated, the field won't be update.
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True, blank=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    # used if user click Read More button
    def get_absolute_url(self):
        return reverse('blog', kwargs={
            'blog_id': self.id
        })