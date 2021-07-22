from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class showinfo(admin.ModelAdmin):
    list_display=('Name','Email','Contact','Messages')
