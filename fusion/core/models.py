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
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Estatísticas')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Camadas')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete'))
    )
    service = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(choices=ICONE_SERVICES, max_length=50)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(max_length=130)

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')
        ordering = ['id']

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField(max_length=120)
    position = models.ForeignKey(Position, related_name='employess', on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    image = StdImageField(upload_to=shuffle_filename, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(max_length=60, default='#')
    twitter = models.CharField(max_length=60, default='#')
    instagram = models.CharField(max_length=60, default='#')

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['id']

    def __str__(self):
        return self.name


class Feature(Base):
    ICONES_FEATURES = (
        ('lni-rocket', _('Foguete')),
        ('lni-laptop-phone', _('API')),
        ('lni-cog', _('Engrenagem')),
        ('lni-leaf', _('Folha')),
        ('lni-layers', _('Camadas')),
        ('lni-leaf', _('Folha')),
    )
    feature = models.CharField(max_length=120)
    description = models.TextField(default='', blank=True)
    icon = models.CharField(max_length=60, choices=ICONES_FEATURES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.feature
