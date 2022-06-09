from django.contrib import admin

from clothes.models import Clothes, Categoria, Size

# Register your models here.
@admin.register(Clothes)
class clothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'bar_code', 'is_active']



admin.site.register(Categoria)

admin.site.register(Size)