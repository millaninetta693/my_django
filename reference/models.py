from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from taggit.managers import TaggableManager


class Reference(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'reference_posts')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)

    objects = models.Manager()

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
    #     #return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
        return reverse_lazy('reference:reference_list')

# Create your models here.
