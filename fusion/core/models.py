from django.db import models
from stdimage.models import StdImageField  # noqa
import uuid


def shuffle_filename(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

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
    position = models.ForeignKey(Position, related_name='employess', on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
