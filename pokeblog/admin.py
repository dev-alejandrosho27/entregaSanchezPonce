from django.contrib import admin
from .models import Tipos,Reviews

# Register your models here.



class ReviewAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
    
class TiposAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
    
admin.site.register(Reviews,ReviewAdmin)
admin.site.register(Tipos,TiposAdmin)