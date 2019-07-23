from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

class Tag(models.Model):
    """Tag model"""
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        db_table = 'tag'
        ordering = ('name',)

    def __str__(self):
        return u'%s' % self.name


class Card(models.Model):
    """Card model"""
    BAR = 1
    RETAIL = 2
    OTHER = 3
    KIND_CHOICES = (
        (BAR, 'bar'),
        (RETAIL, 'retail'),
        (OTHER, 'other'),
    )
    dt = models.DateTimeField(auto_now_add=True)
    dtMod = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, unique=True)
    name = models.CharField(max_length=255, verbose_name="Name")
    kind = models.IntegerField(choices=KIND_CHOICES, default=OTHER, verbose_name="Type")
    description = models.TextField(verbose_name="Description")
    logo = models.ImageField(null=False, upload_to='cards/logos', max_length=24576, verbose_name="Logo")
    image = models.ImageField(null=False, upload_to='cards/img', max_length=24576, verbose_name="Image")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="tags")

    class Meta:
        db_table = 'card'
        ordering = ('name',)

    def __str__(self):
        return u'%s' % self.name


@receiver(post_delete, sender=Card)
def ficha_delete(sender, instance, **kwargs):
    """Delete cards static files"""
    instance.image.delete(False)
    instance.logo.delete(False)
