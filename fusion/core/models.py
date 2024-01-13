from django.db import models
from stdimage.models import StdImageField  # noqa
import uuid


def shuffle_filename(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Service(Base):
    SERVICES_ICONS = (
        ('lni-cog', 'Cog'),
        ('lni-stats-up', 'Stats'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Layers'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket')
    )
    service = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(choices=SERVICES_ICONS, max_length=50)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['id', ]

    def __str__(self):
        return self.service


class Role(Base):
    role = models.CharField(max_length=130)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['id']

    def __str__(self):
        return self.role


class Employee(Base):
    name = models.CharField(max_length=120)
    role = models.ForeignKey(Role, related_name='employees', on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    image = StdImageField(upload_to=shuffle_filename, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(max_length=60, default='#')
    twitter = models.CharField(max_length=60, default='#')
    instagram = models.CharField(max_length=60, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        return self.name


class Feature(Base):
    FEATURES_ICONS = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'API'),
        ('lni-cog', 'Cog'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
        ('lni-leaf', 'Leaf'),
    )
    feature = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(max_length=60, choices=FEATURES_ICONS)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
        ordering = ['id', ]

    def __str__(self):
        return self.feature
