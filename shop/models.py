from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('REEL', 'Reels'),
    ('ROD', 'Rods'),
    ('TACKLE', 'Tackle')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

TAG_CHOICES = (
    ('N', 'NEW'),
    ('L', 'LOW STOCK'),
    ('P', 'ON SALE'),
    ('S', 'SOLD OUT')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    tag = models.CharField(choices=TAG_CHOICES, max_length=1)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_product_url(self):
        return reverse("shop:product", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
