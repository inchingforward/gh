from django.db import models

class CoworkingSpace(models.Model):
    name = models.TextField()
    url = models.URLField()
    address = models.TextField()
    details = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/coworking/%s/" % self.id

    