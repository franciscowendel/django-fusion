from django.db import models
from stdimage.models import StdImageField  # noqa
from django.utils.translation import gettext_lazy as _
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
    ICONE_SERVICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Estatísticas'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Camadas'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete')
    )
    service = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(choices=ICONE_SERVICES, max_length=50)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(max_length=130)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
        ordering = ['id']

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField(max_length=120)
    position = models.ForeignKey(Position, related_name='employees', on_delete=models.CASCADE)
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
    ICONES_FEATURES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'API'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
        ('lni-leaf', 'Folha'),
    )
    feature = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(max_length=60, choices=ICONES_FEATURES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature
