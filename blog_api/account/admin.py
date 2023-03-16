from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.


User = get_user_model() # обращаемся конкретно к тому юзеру которого мы создали! чтобы не создавать общую модель юзера
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff')
    list_filter = (('is_staff', admin.BooleanFieldListFilter),)

