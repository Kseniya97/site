from  django.contrib import  admin
from  price.models import *
class WomanAdmin(admin.ModelAdmin):
    search_fields = ["ycluga"]
    list_display = ('ycluga','price',)
admin.site.register(Woman, WomanAdmin)
class ManAdmin(admin.ModelAdmin):
    search_fields = ["ycluga"]
    list_display = ('ycluga', 'price',)
admin.site.register(Man, ManAdmin)
class DlinnaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dlinna, DlinnaAdmin)
class NailsAdmin(admin.ModelAdmin):
    search_fields = ["ycluga"]
    list_display = ('ycluga', 'price',)
admin.site.register(Nails, NailsAdmin)
class Nails_typeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nails_type,Nails_typeAdmin)
class OtherAdmin(admin.ModelAdmin):
    search_fields = ["ycluga"]
    list_display = ('ycluga', 'price',)
admin.site.register(Other, OtherAdmin)
class Other_typeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Other_type,Other_typeAdmin)

