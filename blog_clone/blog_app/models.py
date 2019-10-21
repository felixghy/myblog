from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    #auth = models.ForeignKey(User,on_delete=models.CASCADE)
    auth = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date =  models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    # if no date it means this post is draft. now showing up
    # jose code: argument in dateime field(blank=true, null=true)

    def approved_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("blog_app1:post_detail",kwargs={'pk':self.pk})
    #jose def approve_comments(self):
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
        print(f'post object is saved. publish date is {self.publish_date}')
    def __str__(self):
        return self.title

class Comment(models.Model):
    """docstring for Comment."""
    #different from Jose 'Blog.post'
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    auth = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)
    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
            return reverse("blog_app1:post_list")
    def __str__(self):
        return self.text
