from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile_photo', 'email', ) # указываем названия полей как в модели
    list_editable = ('profile_photo', )