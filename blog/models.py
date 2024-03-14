from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse



CATEGORY_CHOICES = (
    ('NEWS', 'News'),
    ('FISHING_TRIPS', 'Fishing Trips'),
    ('TACKLE', 'Tackle')
)

TAG_CHOICES = (
    ('ORVIS', 'Orvis'),
    ('SAVAGE_GEAR', 'Savage Gear'),
    ('SHIMANO', 'Shimano'),
    ('SAGE', 'Sage')
)

class Post(models.Model):
    """ Blog post model """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    tags = models.CharField(max_length=20, choices=TAG_CHOICES, null=True, blank=True)
    categories = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Override the save method to generate slug from title """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """ Get the absolute URL of the post """
        return reverse('post_detail', args=[str(self.slug)])
