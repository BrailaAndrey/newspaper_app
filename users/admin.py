from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # переопределяем
    form = CustomUserChangeForm  # переопределяем
    model = CustomUser
    list_display = ['email', 'last_login', 'date_joined', 'username', 'age', 'is_staff', ]
    #list_filter = ('email', 'last_login', )


admin.site.register(CustomUser, CustomUserAdmin)
