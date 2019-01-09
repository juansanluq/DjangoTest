from django.contrib import admin

# Register your models here.
from beers.models import Beer, Company

class BeerAdmin(admin.ModelAdmin):
    list_display = ("name","abv","is_filtered")
    list_filter = ("is_filtered",)
    exclude = ("created_by","last_modified_by")


admin.site.register(Beer,BeerAdmin)
admin.site.register(Company)