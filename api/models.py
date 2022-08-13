from django.db import models
from django.utils.text import slugify

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    toy_category = models.CharField(max_length=200,blank=True, default='')
    was_included_in_home = models.BooleanField(default=False)
    release_date = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # if not self.slug:
        super().save(*args, **kwargs)