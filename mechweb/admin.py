from django.contrib import admin
from django.contrib.auth.admin import UserAdmin# as BaseUserAdmin
from .models import CustomUser, StudentPage, StudentHomePage
from import_export import resources
from .constants import USER_TYPES
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

# If you use this then comment the code in forms 
# -------------------------------------------------
# class CustomUserInline(admin.StackedInline):
# 	model = CustomUser
# 	can_delete = False

# class UserAdmin(BaseUserAdmin):
# 	inlines = [CustomUserInline]
# -------------------------------------------------
admin.site.register(CustomUser, UserAdmin)

# class StudentPageInline(admin.StackedInline):
#     model = StudentPage

# class StudentPageAdmin(ModelAdmin):
#     model = StudentPage
#     inlines=[
#         StudentPageInline,
#     ]
# modeladmin_register(StudentPageAdmin)


# app/admin.py

class CustomUserResource(resources.ModelResource):

    class Meta:
        model = CustomUser
        """
		By default all records will be imported, even if no changes are detected. This can be changed setting the skip_unchanged option. Also, the report_skipped option controls whether skipped records appear in the import Result object, and if using the admin whether skipped records will show in the import preview page:
        """
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('username',)
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'user_type', 'uid')
        export_order = ('username', 'first_name', 'last_name', 'email', 'user_type', 'uid')

    def dehydrate_user_type(self, user):
    	return USER_TYPES[int(user.user_type)][1]

# from mechweb.admin import CustomUserResource
# dataset = CustomUserResource().export()
# print(dataset.csv)