from django.contrib import admin
from django.contrib.auth.admin import UserAdmin# as BaseUserAdmin
from .models import CustomUser, MechHomePage, Aboutiitgmech, EventHomePage, EventPage, CategoriesHome, Categories, FacultyHomePage, FacultyPage, StudentHomePage, StudentPage, StaffHomePage, StaffPage, AlumniHomePage, AlumnusPage, ResearchHomePage, ResearchLabHomePage, ResearchLabPage, PublicationHomePage, PublicationPage, ProjectHomePage, ProjectPage, CourseStructure, CoursePage, AwardHomePage
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



class MechHomePageResource( resources.ModelResource):
    class Meta:
        model= MechHomePage
        skip_unchanged = True
        report_skipped = False

class AboutiitgmechResource( resources.ModelResource):
    class Meta:
        model= Aboutiitgmech
        skip_unchanged = True
        report_skipped = False

class EventHomePageResource( resources.ModelResource):
    class Meta:
        model= EventHomePage
        skip_unchanged = True
        report_skipped = False

class EventPageResource( resources.ModelResource):
    class Meta:
        model= EventPage
        skip_unchanged = True
        report_skipped = False

class CategoriesHomeResource( resources.ModelResource):
    class Meta:
        model= CategoriesHome
        skip_unchanged = True
        report_skipped = False

class CategoriesResource( resources.ModelResource):
    class Meta:
        model= Categories
        skip_unchanged = True
        report_skipped = False

class FacultyHomePageResource( resources.ModelResource):
    class Meta:
        model= FacultyHomePage
        skip_unchanged = True
        report_skipped = False

class FacultyPageResource( resources.ModelResource):
    class Meta:
        model= FacultyPage
        skip_unchanged = True
        report_skipped = False

class StudentHomePageResource( resources.ModelResource):
    class Meta:
        model= StudentHomePage
        skip_unchanged = True
        report_skipped = False

class StudentPageResource( resources.ModelResource):
    class Meta:
        model= StudentPage
        skip_unchanged = True
        report_skipped = False

class StaffHomePageResource( resources.ModelResource):
    class Meta:
        model= StaffHomePage
        skip_unchanged = True
        report_skipped = False

class StaffPageResource( resources.ModelResource):
    class Meta:
        model= StaffPage
        skip_unchanged = True
        report_skipped = False

class AlumniHomePageResource( resources.ModelResource):
    class Meta:
        model= AlumniHomePage
        skip_unchanged = True
        report_skipped = False

class AlumnusPageResource( resources.ModelResource):
    class Meta:
        model= AlumnusPage
        skip_unchanged = True
        report_skipped = False

class ResearchHomePageResource( resources.ModelResource):
    class Meta:
        model= ResearchHomePage
        skip_unchanged = True
        report_skipped = False

class ResearchLabHomePageResource( resources.ModelResource):
    class Meta:
        model= ResearchLabHomePage
        skip_unchanged = True
        report_skipped = False

class ResearchLabPageResource( resources.ModelResource):
    class Meta:
        model= ResearchLabPage
        skip_unchanged = True
        report_skipped = False

class PublicationHomePageResource( resources.ModelResource):
    class Meta:
        model= PublicationHomePage
        skip_unchanged = True
        report_skipped = False

class PublicationPageResource( resources.ModelResource):
    class Meta:
        model= PublicationPage
        skip_unchanged = True
        report_skipped = False

class ProjectHomePageResource( resources.ModelResource):
    class Meta:
        model= ProjectHomePage
        skip_unchanged = True
        report_skipped = False

class ProjectPageResource( resources.ModelResource):
    class Meta:
        model= ProjectPage
        skip_unchanged = True
        report_skipped = False

class CourseStructureResource( resources.ModelResource):
    class Meta:
        model= CourseStructure
        skip_unchanged = True
        report_skipped = False

class CoursePageResource( resources.ModelResource):
    class Meta:
        model= CoursePage
        skip_unchanged = True
        report_skipped = False

class AwardHomePageResource( resources.ModelResource):
    class Meta:
        model= AwardHomePage
        skip_unchanged = True
        report_skipped = False

# MechHomePage
# Aboutiitgmech
# EventHomePage
# EventPage
# CategoriesHome
# Categories
# FacultyHomePage
# FacultyPage
# StudentHomePage
# StudentPage
# StaffHomePage
# StaffPage
# AlumniHomePage
# AlumnusPage
# ResearchHomePage
# ResearchLabHomePage
# ResearchLabPage
# PublicationHomePage
# PublicationPage
# ProjectHomePage
# ProjectPage
# CourseStructure
# CoursePage
# AwardHomePage

# from mechweb.admin import CustomUserResource
# dataset = CustomUserResource().export()
# print(dataset.csv)

# from mechweb.admin import CustomUserResource
# CustomUser_dataset = CustomUserResource().export()
# print(CustomUser_dataset.csv)

# from mechweb.admin import MechHomePageResource
# MechHomePage_dataset = MechHomePageResource().export()
# print(MechHomePage_dataset.csv)

# from mechweb.admin import AboutiitgmechResource
# Aboutiitgmech_dataset = AboutiitgmechResource().export()
# print(Aboutiitgmech_dataset.csv)

# from mechweb.admin import EventHomePageResource
# EventHomePage_dataset = EventHomePageResource().export()
# print(EventHomePage_dataset.csv)

# from mechweb.admin import EventPageResource
# EventPage_dataset = EventPageResource().export()
# print(EventPage_dataset.csv)

# from mechweb.admin import CategoriesHomeResource
# CategoriesHome_dataset = CategoriesHomeResource().export()
# print(CategoriesHome_dataset.csv)

# from mechweb.admin import CategoriesResource
# Categories_dataset = CategoriesResource().export()
# print(Categories_dataset.csv)

# from mechweb.admin import FacultyHomePageResource
# FacultyHomePage_dataset = FacultyHomePageResource().export()
# print(FacultyHomePage_dataset.csv)

# from mechweb.admin import FacultyPageResource
# FacultyPage_dataset = FacultyPageResource().export()
# print(FacultyPage_dataset.csv)

# from mechweb.admin import StudentHomePageResource
# StudentHomePage_dataset = StudentHomePageResource().export()
# print(StudentHomePage_dataset.csv)

# from mechweb.admin import StudentPageResource
# StudentPage_dataset = StudentPageResource().export()
# print(StudentPage_dataset.csv)

# from mechweb.admin import StaffHomePageResource
# StaffHomePage_dataset = StaffHomePageResource().export()
# print(StaffHomePage_dataset.csv)

# from mechweb.admin import StaffPageResource
# StaffPage_dataset = StaffPageResource().export()
# print(StaffPage_dataset.csv)

# from mechweb.admin import AlumniHomePageResource
# AlumniHomePage_dataset = AlumniHomePageResource().export()
# print(AlumniHomePage_dataset.csv)

# from mechweb.admin import AlumnusPageResource
# AlumnusPage_dataset = AlumnusPageResource().export()
# print(AlumnusPage_dataset.csv)

# from mechweb.admin import ResearchHomePageResource
# ResearchHomePage_dataset = ResearchHomePageResource().export()
# print(ResearchHomePage_dataset.csv)

# from mechweb.admin import ResearchLabHomePageResource
# ResearchLabHomePage_dataset = ResearchLabHomePageResource().export()
# print(ResearchLabHomePage_dataset.csv)

# from mechweb.admin import ResearchLabPageResource
# ResearchLabPage_dataset = ResearchLabPageResource().export()
# print(ResearchLabPage_dataset.csv)

# from mechweb.admin import PublicationHomePageResource
# PublicationHomePage_dataset = PublicationHomePageResource().export()
# print(PublicationHomePage_dataset.csv)

# from mechweb.admin import PublicationPageResource
# PublicationPage_dataset = PublicationPageResource().export()
# print(PublicationPage_dataset.csv)

# from mechweb.admin import ProjectHomePageResource
# ProjectHomePage_dataset = ProjectHomePageResource().export()
# print(ProjectHomePage_dataset.csv)

# from mechweb.admin import ProjectPageResource
# ProjectPage_dataset = ProjectPageResource().export()
# print(ProjectPage_dataset.csv)

# from mechweb.admin import CourseStructureResource
# CourseStructure_dataset = CourseStructureResource().export()
# print(CourseStructure_dataset.csv)

# from mechweb.admin import CoursePageResource
# CoursePage_dataset = CoursePageResource().export()
# print(CoursePage_dataset.csv)

# from mechweb.admin import AwardHomePageResource
# AwardHomePage_dataset = AwardHomePageResource().export()
# print(AwardHomePage_dataset.csv)