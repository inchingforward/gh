from urlparse import urlparse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import tweepy


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
    
    def get_domain(self):
        return urlparse(self.url).netloc
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        
        if settings.TWITTER_CONSUMER_KEY:
            try:
                auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
                auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
                
                api = tweepy.API(auth)
                api.update_status("%s %s" % (self.title[0:115], self.url))
            except:
                pass

