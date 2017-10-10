from django.contrib import admin
from modelphone import models
class ProductAdmin(admin.ModelAdmin):
    list_display=('pmodel','nicename','year','price')
    search_fields=('nicename',)
    ordering = ('-price',)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.PPhoto)
