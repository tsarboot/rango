from django.contrib import admin
from rango.models import UserProfil
from rango.models import Category,Car

class CategoryAdmin(admin.ModelAdmin):
    fields = ["likes","name","views"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Car)
admin.site.register(UserProfil)

