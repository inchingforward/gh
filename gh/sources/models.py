from django.db import models


class WebPage(models.model):
    title = models.TextField()
    url = models.URLField()
    selector = models.TextField()
    prefix = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-title']
    
    def __unicode__(self):
        return self.title
