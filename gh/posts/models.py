from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    url = models.URLField(blank=True)
    title = models.TextField()
    details = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/posts/%s/" % self.id
