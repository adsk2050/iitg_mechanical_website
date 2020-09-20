
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin# as BaseUserAdmin
# from django.contrib.auth.models import Permission
from .models import CustomUser
# , MechHomePage, Aboutiitgmech, EventHomePage, EventPage, CategoriesHome, Categories, FacultyHomePage, FacultyPage, StudentHomePage, StudentPage, StaffHomePage, StaffPage, AlumniHomePage, AlumnusPage, ResearchHomePage, ResearchLabHomePage, ResearchLabPage, PublicationHomePage, PublicationPage, ProjectHomePage, ProjectPage, CourseStructure, CoursePage, AwardHomePage

admin.site.register(CustomUser, UserAdmin)
