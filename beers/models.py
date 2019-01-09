from django.db import models
from PIL import Image

# Create your models here.
from beers.utils import image_upload_location
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Nombre', max_length=50)
    tax_number = models.IntegerField('Tax number',unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-name']

    def __str__(self):
        return self.name



class Beer(CommonInfo):
    COLOR_AMARILLO = 1
    COLOR_NEGRO = 2
    COLOR_AMBAR = 3
    COLOR_MARRON = 4

    COLOR_CHOICES = (
        (COLOR_AMARILLO, 'amarillo'),
        (COLOR_NEGRO, 'negro'),
        (COLOR_AMBAR, 'ámbar'),
        (COLOR_MARRON, 'marron'),
    )

    name = models.CharField('Nombre', max_length=50)
    descripcion = models.CharField('Descripción', max_length=250,default="Introduce una descripción para la cerveza, por defecto mantendrá esta")
    abv = models.DecimalField('Alcohol by volumen',max_digits=5,decimal_places=2, default= 0)
    is_filtered = models.BooleanField('Is filtered?',default=False)
    color = models.SmallIntegerField('Color',choices=COLOR_CHOICES,default=COLOR_AMARILLO)
    image = models.ImageField('Imagen', blank=True, null=True, upload_to=image_upload_location,default="/other/images/warning_placeholder.svg")
    company = models.ForeignKey(Company,related_name="beers",on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['created_at']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alchohol_than(self,alcohol):
        return self.abv > alcohol

class SpecialIngredient(CommonInfo):
    name = models.CharField('Nombre', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = "Special ingredient"
        verbose_name_plural = "Special ingredients"
        ordering = ['-name']

    def __str__(self):
        return self.name