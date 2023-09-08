from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    description=models.ImageField(verbose_name='Descripcion')
    image=models.ImageField(verbose_name='imagen', upload_to='projects')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaciom')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']

    def __str__(self):
        return self.title3