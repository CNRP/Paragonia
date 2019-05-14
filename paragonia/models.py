from django.db import models

class GuideSection(models.Model):
    title = models.CharField(max_length=40)
    thumbnail_url = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name_plural = "Guides"

class HomeSection(models.Model):
    title = models.CharField(max_length=40)
    thumbnail_url = models.CharField(max_length=50)
    content = models.TextField()
    align = models.CharField(max_length=5)
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name_plural = "Home Sections"
