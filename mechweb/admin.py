from django.contrib import admin
from django.contrib.auth.admin import UserAdmin# as BaseUserAdmin
from .models import CustomUser

# If you use this then comment the code in forms 
# -------------------------------------------------
# class CustomUserInline(admin.StackedInline):
# 	model = CustomUser
# 	can_delete = False

# class UserAdmin(BaseUserAdmin):
# 	inlines = [CustomUserInline]
# -------------------------------------------------

admin.site.register(CustomUser, UserAdmin)