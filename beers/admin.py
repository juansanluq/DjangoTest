from django.contrib import admin

# Register your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from beers.models import Beer, Company

class BeerAdmin(admin.ModelAdmin):
    list_display = ("name","abv","is_filtered","image")
    list_filter = ("is_filtered",)
    exclude = ("created_by","last_modified_by")


admin.site.register(Beer,BeerAdmin)
admin.site.register(Company)

@receiver(post_save, sender=Beer)
def my_handler(sender, **kwargs):
    print('post save callback')