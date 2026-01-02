import uuid
from django.db import models

from stdimage.models import StdImageField


# geração de nome único para upload de imagens e arquivos
def upload_to_instance(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateField('Criação', auto_now_add=True)
    updated_at = models.DateField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Camadas'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Ícone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class JobTitle(Base):
    job_title = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.job_title


class Employee(Base):
    name = models.CharField('Nome', max_length=100)
    job_title = models.ForeignKey('core.JobTitle',
                                  verbose_name='Cargo',
                                  on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    photo = StdImageField(
        'Foto',
        upload_to=upload_to_instance,
        variations={
            'thumb': {
                'width': 480,
                'height': 480,
                'crop': True
            }
        }
    )
    facebook = models.CharField('Facebook', max_length=200, default='#')
    instagram = models.CharField('Instagram', max_length=200, default='#')
    linkedin = models.CharField('Linkedin', max_length=200, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name


class FeaturedItem(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop e Telefone'),
        ('lni-cup', 'Copo'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
        ('lni-briefcase', 'Mala'),
    )
    feature = models.CharField('Recurso', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Ícone', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Item em Destaque'
        verbose_name_plural = 'Itens em Destaque'

    def __str__(self):
        return self.feature
