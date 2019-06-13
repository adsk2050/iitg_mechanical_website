from django.contrib import admin
from django.contrib.auth.admin import UserAdmin# as BaseUserAdmin
from .models import CustomUser
from import_export import resources


# If you use this then comment the code in forms 
# -------------------------------------------------
# class CustomUserInline(admin.StackedInline):
# 	model = CustomUser
# 	can_delete = False

# class UserAdmin(BaseUserAdmin):
# 	inlines = [CustomUserInline]
# -------------------------------------------------

admin.site.register(CustomUser, UserAdmin)

# app/admin.py

# class CustomUserResource(resources.ModelResource):

#     class Meta:
#         model = CustomUser
#         skip_unchanged = True
#         report_skipped = False
#         import_id_fields = ('isbn',) #The default field for object identification is id, you can optionally set which fields are used as the id when importing:
#         fields = ('id', 'name', 'price',)
#         export_order = ('id', 'price', 'author', 'name')
#         exclude = ('imported', )