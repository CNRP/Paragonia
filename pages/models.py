from django.db import models
from datetime import datetime

class NewsPost(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    thumbnail_url = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        return "("+str(self.id)+") " + self.title
    class Meta: 
        verbose_name_plural = "News"
