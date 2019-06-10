from datetime import datetime

from django.db import models
from django import forms
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator


from django.utils.text import slugify
# from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
######################################################

from wagtailautocomplete.edit_handlers import AutocompletePanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldRowPanel, FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from modelcluster.fields import ParentalKey
######################################################


from wagtail.documents.edit_handlers import DocumentChooserPanel

######################################################
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.images.edit_handlers import ImageChooserPanel

######################################################
# for tagging
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag
######################################################
# Importing constants and settings
from iitg_mechanical_website.settings.base import CUSTOM_RICHTEXT
from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS, EVENTS, STUDENT_PROGRAMME, MASTERS_SPECIALIZATION, STAFF_DESIGNATION, PROJECT_TYPES, PUBLICATION_TYPES, LAB_TYPES, LAB_RESEARCH_AREAS, COURSE_TYPES, USER_TYPES
# , NAV_ORDER

from .constants import DISPOSAL_COMMITTEE, LABORATORY_IN_CHARGE, FACULTY_IN_CHARGE, DISCIPLINARY_COMMITTEE, DUPC, DPPC,FACULTY_DESIGNATION, FACULTY_ROLES, FACULTY_AWARD_TYPES

######################################################

#Need to work on how URLs work in wagtail. Can't access the pages !!!

######################################################
# when makemigrations are happening this does not show as change in the db
# class CustomUserManager(BaseUserManager):
# 	def create_user(self, username, user_type, password):
# 		if not user_type:
# 			raise ValueError('Must provide user_type')
# 		user = self.model(
# 			user_type=user_type,
# 		)
# 		if password
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user

# 	def create_superuser(self, user_type, password):
# 		user = self.model(
# 			user_type=user_type
# 		)
# 		user.set_password(password)
# 		user.is_admin=True
# 		user.save(using=self._db)
# 		return user

# 	def has_perm(self, perm, obj=None):
# 		""" Does this user have a specific permission"""
# 		#Simplest possible answer - always true
# 		return True

# 	def has_module_perm(self, app_label):
# 		"""Does the user have the permissions to view the app "app_label"? """
# 		# simplest answer - yes always
# 		return True

# 	@property
# 	def is_staff(self):
# 			"""Is the user a member of staff?"""
# 			#simplest answer - All admins are staff
# 			return self._is_admin

class CustomUser(AbstractUser):
	# pass
	is_admin = models.BooleanField(default=False)
	# is_staff = models.BooleanField(default=True)
	user_type = models.CharField(max_length=2, choices=USER_TYPES, default='0')
	# USERNAME_FIELD = 'username' # Its anyway the default, but you can change this 

######################################################
class MechHomePage(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	# intro = RichTextField(blank=True)
	# user = models.OneToOneField(CustomUser, related_name='mech_home_page_manager', null=True, on_delete=models.SET_NULL)
	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full"),
		InlinePanel('gallery_images', label="Gallery Images"),
	]

	notification_tab_panels = [
		InlinePanel('text_panels', label="Mini Articles", min_num=1),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(notification_tab_panels, heading="News & Notifications"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	subpage_types=['EventHomePage', 'FacultyHomePage', 'StudentHomePage', 'ResearchHomePage', 'StaffHomePage', 'CourseStructure', 'AlumniHomePage', 'AwardHomePage']

	max_count = 1

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		navlist = self.get_children().live().order_by('-first_published_at')
		context['navlist'] = navlist
		return context

	class Meta:
		verbose_name = "Home"

class HomeTextPanel(Orderable):
	page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='text_panels')
	title = models.CharField(blank=True, max_length=50)
	photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
	# You are trying to change the nullable field 'photo' on hometextpanel to non-nullable without a default; we can't do that (the database needs something to populate existing rows).
	# Please select a fix:
	# 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
	# 2) Ignore for now, and let me handle existing rows with NULL myself (e.g. because you added a RunPython or RunSQL operation to handle NULL values in a previous data migration)
	# 3) Quit, and let me add a default in models.py
	# Select an option: 2
	description = models.CharField(blank=True, max_length=500)
	date = models.DateTimeField()
	#change the below content_type code to manage css accordingly
	content_type=models.CharField(
		default="0",
		choices=TEXT_PANEL_CONTENT_TYPES,
		max_length=50
	)
	panels = [
		FieldPanel('title'),
		FieldPanel('description'),
		FieldPanel('date'),
		FieldPanel('content_type'),
		ImageChooserPanel('photo'),
	]

class MechHomePageGalleryImage(Orderable):
	page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='gallery_images')
	photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('photo'),
			FieldPanel('caption'),
		]),
	]

######################################################
class EventHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[0])
	# user = models.OneToOneField(CustomUser, related_name='event_home_page_manager', null=True, on_delete=models.SET_NULL)
	featured_event = models.ForeignKey(
		'EventPage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='featured_event'
	)
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

	content_panels = Page.content_panels + [
			FieldPanel('intro'),
			AutocompletePanel('featured_event'),
			#InlinePanel('event_page', label="New Event"),
		]

	parent_page_types=['MechHomePage']
	subpage_types=['EventPage']
	max_count = 1

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		event_list = self.get_children().live().order_by('-first_published_at')
		paginator = Paginator(event_list, 1) # Show 1 events per page
		page = request.GET.get('page')
		event_list = paginator.get_page(page)
		context['event_list'] = event_list
		return context

	class Meta:
		verbose_name = "Event Home"

class EventPage(Page):
	# user = models.ForeignKey('CustomUser', related_name='event_manager', null=True, on_delete=models.SET_NULL)
	event_name = models.CharField(blank=True, max_length=50)
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	start_date = models.DateTimeField(default=timezone.now)
	end_date = models.DateTimeField()
	venue = models.CharField(blank=True, max_length=50, choices=LOCATIONS, default='0')
	poster = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	event_type = models.CharField(max_length=50, choices=EVENTS, default='0')
	content_panels = Page.content_panels + [
		FieldPanel('event_type'),
		FieldPanel('event_name'),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('start_date'),
				FieldPanel('end_date'),
			]),
		],  heading="Timings"),
		FieldPanel('venue'),
		FieldPanel('description'),
		FieldRowPanel([
			ImageChooserPanel('poster'),
			DocumentChooserPanel('document'),
		]),
		InlinePanel('gallery_images', label="Gallery Images", max_num=2),
		InlinePanel('links', label="Related Links", max_num=10),
	]

	# promote_panels=[]
	# settings_panels=[]

	parent_page_types=['EventHomePage']
	subpage_types=[]
	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

class EventPageGalleryImage(Orderable):
	page = ParentalKey(EventPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image',
		on_delete=models.CASCADE,
		related_name='+'
	)
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('image'),
			FieldPanel('caption'),
		]),
	]

class EventPageLink(Orderable):
	page = ParentalKey(EventPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

######################################################
# Can I make a generic class which covers all these repeatedly adding of data models needed to be written only once?
######################################################

class FacultyHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[1])
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

	content_panels = Page.content_panels + [
			FieldPanel('intro'),
		]

	parent_page_types=['MechHomePage']
	subpage_types=['FacultyPage']
	max_count = 1

	# This function is not working here
	# def list_common_interests(self):
	
	def serve(self, request):
		faculty_list = self.get_children().live().order_by('facultypage__first_name', 'facultypage__last_name')

		all_research_interests = faculty_interests()

		tag = request.GET.get('tag')
		if tag:
			faculty_list = faculty_list.filter(facultypage__research_interests__name=tag)
				#check this bro!! what is name?? both models faculty page or facultyhomepage or facultyresearchinteresttag  dont have name keyword... maybe name keyword is in clustertaggablemanager source code 
		paginator = Paginator(faculty_list, 1) # Show 10 faculty per page
		page_no = request.GET.get('page_no')
		faculty_list = paginator.get_page(page_no)

		return render(request, self.template, {
			'page': self,
			'faculty_list': faculty_list,
			'all_research_interests': all_research_interests,
			'tag':tag,
			'page_no':page_no,
		})

		class Meta:
			verbose_name = "Faculty Home"

class FacultyResearchInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'FacultyPage',
		related_name='tagged_items',
		on_delete=models.CASCADE )
	# This function is working here only in shell but not during rendering
	# def list_common_interests(self):

class FacultyPage(Page):
	user = models.OneToOneField(CustomUser, related_name='faculty', null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	office_contact_number = models.CharField(max_length=20, blank=True)
	home_contact_number = models.CharField(max_length=20, blank=True)
	office_address_line_1 = models.CharField(max_length=25, blank=True)
	home_address_line_1 = models.CharField(max_length=25, blank=True)
	email_id = models.EmailField(unique=True)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250, blank=True)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT) 
	research_interests = ClusterTaggableManager(through=FacultyResearchInterestTag, blank=True, verbose_name='Research Interests')
	joining_date = models.DateField(default=timezone.now)
	leaving_date = models.DateField(blank=True, null=True)
	designation = models.CharField(max_length=2, choices=FACULTY_DESIGNATION, default='3')
	website = models.URLField(max_length=250)
	#################################################################

	additional_roles = models.CharField(max_length=2, choices=FACULTY_ROLES, default='2')
	disposal_committee = models.CharField(max_length=2, choices=DISPOSAL_COMMITTEE, default='4')
	laboratory_in_charge = models.CharField(max_length=2, choices=LABORATORY_IN_CHARGE, default='14')
	faculty_in_charge = models.CharField(max_length=2, choices=FACULTY_IN_CHARGE, default='11')
	disciplinary_committee = models.CharField(max_length=2, choices=DISCIPLINARY_COMMITTEE, default='4')
	dupc = models.CharField(max_length=2, choices=DUPC, default='6')
	dppc = models.CharField(max_length=2, choices=DPPC, default='6')

	#################################################################
	content_panels = Page.content_panels + [
		######################################################
		# The user should not be able to change these things from here
		FieldPanel('user'),
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('email_id'), 
		######################################################
		FieldPanel('designation'),
		FieldPanel('joining_date'),
		FieldPanel('website'),

		MultiFieldPanel([
			FieldPanel('office_address_line_1'),
			FieldPanel('office_contact_number'),

		], heading="Office Address"),
		MultiFieldPanel([
			FieldPanel('home_address_line_1'),
			FieldPanel('home_contact_number'),
		], heading="Residence Address"),

		ImageChooserPanel('photo'),
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('research_interests'),
		InlinePanel('gallery_images', label="Gallery images", max_num=10),
		FieldPanel('leaving_date'),
	]
	# Creating custom tabs
	custom_tab_panels = [
		FieldPanel('additional_roles'),
		FieldPanel('laboratory_in_charge'),
		FieldPanel('faculty_in_charge'),
		FieldPanel('dupc'),
		FieldPanel('dppc'),
		FieldPanel('disciplinary_committee'),
		FieldPanel('disposal_committee'),
	]

	achievement_tab_panels= [
		InlinePanel('fac_award', label="Awards"),
	]

	announcement_tab_panels = [
		InlinePanel('faculty_announcement', label="Announcement", max_num=10),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(custom_tab_panels, heading="Administration"),
		ObjectList(announcement_tab_panels, heading="Announcement"),
		ObjectList(achievement_tab_panels, heading="Achievements"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	def __str__(self):
		return self.first_name+" "+self.last_name

	def get_context(self, request):
		lab_relation_list = self.faculty_lab.all()
		lab_incharge = self.faculty_incharge.all()
		lab_list = []
		for lab in lab_incharge:
			lab_list.append(lab)
		for lab_relation in lab_relation_list:
			lab = lab_relation.page
			lab_list.append(lab)

		pub_relation_list = self.faculty_pub.all()
		pub_list = []
		for pub_relation in pub_relation_list:
			pub = pub_relation.page
			pub_list.append(pub)

		project_relation_list = self.faculty_co_investigator.all()
		project_pi =  self.principal_investigator.all()
		project_list = []
		for project in project_pi:
			project_list.append(lab)
		for project_relation in project_relation_list:
			project = project_relation.page
			project_list.append(project)

		course_relation_list = self.course_instructor.all()
		course_list = []
		for course_relation in course_relation_list:
			course = course_relation.page
			course_list.append(course)

		context = super().get_context(request)
		context['lab_list'] = lab_list
		context['pub_list'] = pub_list
		context['project_list'] = project_list
		context['course_list'] = course_list
		return context


	parent_page_types=['FacultyHomePage']
	subpage_types=[]

	class Meta:
		verbose_name = "Faculty"
		verbose_name_plural = "Faculty"

class FacultyAnnouncement(Orderable):
	page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='faculty_announcement')
	link = models.URLField(max_length=250)
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	message = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	title = models.CharField(blank=True, max_length=50)
	date = models.DateTimeField(blank=True, default=timezone.now)
	panels = [
		FieldPanel('title'),
		FieldPanel('message'),
		FieldPanel('date'),		
		DocumentChooserPanel('document'),
		FieldPanel('link'),
	]

class FacultyPageGalleryImage(Orderable):
	page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('image'),
			FieldPanel('caption'),
		]),
	]

class FacultyAward(Orderable):
	page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='fac_award')
	award_title = models.CharField(max_length=100)
	award_description = RichTextField(blank=True, features=CUSTOM_RICHTEXT) 
	award_type = models.CharField(max_length=2, choices=FACULTY_AWARD_TYPES, default='0')
	award_time = models.DateField(default=timezone.now)
	conferrer = models.CharField(max_length=100)
	conferrer_description = RichTextField(blank=True, features=CUSTOM_RICHTEXT) 
	image = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	link = models.URLField(max_length=250, blank=True)

	panels = [
		FieldPanel('award_title'),
		FieldPanel('award_description'),
		FieldPanel('award_type'),		
		ImageChooserPanel('image'),
		FieldPanel('award_time'),
		FieldPanel('conferrer'),
		FieldPanel('conferrer_description'),
		FieldPanel('link'),
	]

def faculty_interests():
	live_tags = FacultyResearchInterestTag.objects.all()
	common_tags = []
	for tag in live_tags:
		tag2 = tag.__str__().split('tagged with ', 1)
		tag3 = tag2.pop()
		if tag3 not in common_tags:
			common_tags.append(tag3)
	return common_tags

######################################################
class AbstractStudentHomePage(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StudentPage']
	max_count = 1

	class Meta:
		abstract = True

class AbstractStudentPage(Page):
	user = models.OneToOneField(CustomUser, related_name='student', null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_id = models.EmailField(unique=True)
	roll_no = models.IntegerField(unique=True)
	enrolment_year = models.DateField(default=timezone.now)
	programme = models.CharField(max_length=2, choices=STUDENT_PROGRAMME)

	contact_number = models.CharField(max_length=20, blank=True)
	hostel_address = models.CharField(max_length=25, blank=True)
	specialization = models.CharField(max_length=2, choices=MASTERS_SPECIALIZATION, default='0', help_text="Not Applicable - for B.Tech, PhD and PostDocs")
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250, blank=True)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	website = models.URLField(max_length=250, blank=True)

	def get_roll_value(self):
		return self.roll_no

	# def get_enrolment_year(self):
	# 	roll_no_str = str(self.roll_no)
	# 	enrl_yr = datetime.strptime('Aug 1 20'+roll_no[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
	# 	return enrl_yr


	content_panels = Page.content_panels + [
		######################################################
		# The user should not be able to change these things from here
		FieldPanel('user'),
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('email_id'), 
		FieldPanel('roll_no'),
		FieldPanel('enrolment_year'),
		FieldPanel('programme'),
		######################################################
		FieldPanel('specialization'),
		FieldPanel('website'), 
		FieldPanel('contact_number'),
		FieldPanel('hostel_address'),

		ImageChooserPanel('photo'), 
		FieldPanel('intro'),
		FieldPanel('body'),
	]

	parent_page_types=['StudentHomePage']
	subpage_types=[]

	def __str__(self):
		return self.first_name+" "+self.last_name

	class Meta:
		abstract = True

######################################################
class StudentHomePage(AbstractStudentHomePage):
	def serve(self, request):
		student_list = self.get_children().live().order_by('studentpage__enrolment_year', 'studentpage__first_name', 'studentpage__last_name')

		# Filter by programme
		prog = request.GET.get('prog')
		if prog in ['0','1', '2', '3']:
			student_list = student_list.filter(studentpage__programme=prog)

		# Filter by tag
		tag = request.GET.get('tag')
		if tag:
			student_list = student_list.filter(studentpage__research_interests__name=tag)

		paginator = Paginator(student_list, 10) # Show 10 faculty per page
		page_no = request.GET.get('page_no')
		student_list = paginator.get_page(page_no)

		all_research_interests = student_interests()
		return render(request, self.template, {
			'page': self,
			'student_list': student_list,
			'all_research_interests': all_research_interests,
			'tag':tag,
			'page_no':page_no,
			'prog':prog,
		})

	class Meta:
		verbose_name = "Student Home"

class StudentResearchInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'StudentPage',
		related_name='tagged_items',
		on_delete=models.CASCADE
	)

class StudentPage(AbstractStudentPage):
	faculty_advisor = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_advisor')
	research_interests = ClusterTaggableManager(through=StudentResearchInterestTag, blank=True, verbose_name='Research Interests')

	content_panels = AbstractStudentPage.content_panels + [
		AutocompletePanel('faculty_advisor'),#shouldn't this be with faculty, so that studen't can't change faculty advisor by their own.
		FieldPanel('research_interests'),
		InlinePanel('stud_gallery_images', label="Gallery images", max_num=2),
		InlinePanel('stud_links', label="Related Links", max_num=10),
	]

	project_tab_panels = [
		InlinePanel('projects', label="Projects"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(project_tab_panels, heading="Projects"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	def get_context(self, request):
		lab_relation_list = self.student_lab.all()
		lab_list = []
		for lab_relation in lab_relation_list:
			lab = lab_relation.page
			lab_list.append(lab)

		pub_relation_list = self.student_pub.all()
		pub_list = []
		for pub_relation in pub_relation_list:
			pub = pub_relation.page
			pub_list.append(pub)
		# return lab_list
		context = super().get_context(request)
		context['lab_list'] = lab_list
		context['pub_list'] = pub_list
		return context

	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Students"

class StudentProject(Orderable):
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='projects')
	title = models.CharField(blank=True, max_length=50)
	guide = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='guide')
	co_guide = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='co_guide')
	document = models.ForeignKey('wagtaildocs.Document', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_1 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_2 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_3 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	abstract = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	link = models.URLField(max_length=250, blank=True)
	panels = [
		FieldPanel('title'),
		AutocompletePanel('guide'),
		AutocompletePanel('co_guide'),
		DocumentChooserPanel('document'),
		FieldPanel('abstract'),
		FieldPanel('link'),
		MultiFieldPanel([
			ImageChooserPanel('photo_1'),
			ImageChooserPanel('photo_2'),
			ImageChooserPanel('photo_3'),
		], heading ="Featured Photos")

	]

class StudentPageLink(Orderable):
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='stud_links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

class StudentPageGalleryImage(Orderable):
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='stud_gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('image'),
			FieldPanel('caption'),
		]),
	]

def student_interests():
	live_tags = StudentResearchInterestTag.objects.all()
	common_tags = []
	for tag in live_tags:
		tag2 = tag.__str__().split('tagged with ', 1)
		tag3 = tag2.pop()
		if tag3 not in common_tags:
			common_tags.append(tag3)
	return common_tags

######################################################
class StaffHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[4])
	# use_other_template = models.IntegerField(default = 3)#Find a way to remove this shit without deleting the original entry - had to delete original entry - but not because i specifically wanted to remove it, but because i had to implement user model
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	
	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		# FieldPanel('use_other_template')
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StaffPage']
	max_count = 1

	def serve(self, request):
		staff_list = self.get_children().live().order_by('-first_published_at', 'staffpage__first_name', 'staffpage__last_name')

		# Filter by designation
		desig = request.GET.get('desig')
		if desig in ['0','1', '2', '3']:
			staff_list = staff_list.filter(staffpage__designation=desig)

		# Filter by skills tag
		tag = request.GET.get('tag')
		if tag:
			staff_list = staff_list.filter(staffpage__skills__name=tag)

		paginator = Paginator(staff_list, 10) # Show 10 faculty per page
		page_no = request.GET.get('page_no')
		staff_list = paginator.get_page(page_no)

		all_staff_skills = staff_skills()
		return render(request, self.template, {
			'page': self,
			'staff_list': staff_list,
			'all_staff_skills':all_staff_skills,
			'tag':tag,
			'page_no':page_no,
			'desig':desig,
		})

	# and this too
	# def get_template(self,request):
	# 	return 'mechweb/staff_home_page.html'

	class Meta:
		verbose_name = "Staff Home"

class StaffSkillag(TaggedItemBase):
	content_object = ParentalKey(
		'StaffPage',
		related_name='tagged_items',
		on_delete=models.CASCADE
	)

class StaffPage(Page):
	user = models.OneToOneField(CustomUser, related_name='staff', null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_id = models.EmailField()

	designation = models.CharField(max_length=2, choices=STAFF_DESIGNATION, default='1')
	joining_year = models.DateField(default=timezone.now)
	contact_number = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250, blank=True)
	skills = ClusterTaggableManager(through=StaffSkillag, blank=True, verbose_name='Skills')

	#if lab staff:
	# lab = models.ForeignKey('ResearchLabPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='lab')

	content_panels = Page.content_panels + [
	######################################################
		# The user should not be able to change these things from here
		FieldPanel('user'),
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('email_id'),
	######################################################
		# The user should not be able to change these things from here
		FieldPanel('designation'),
		FieldPanel('joining_year'),
		FieldPanel('contact_number'),
		FieldPanel('address'),
		FieldPanel('intro'),
		ImageChooserPanel('photo'),
		FieldPanel('skills'),
	]

	parent_page_types=['StaffHomePage']
	subpage_types=[]

	class Meta:
		verbose_name = "Staff"
		verbose_name_plural = "Staff"

def staff_skills():
	live_tags = StaffSkillag.objects.all()
	common_tags = []
	for tag in live_tags:
		tag2 = tag.__str__().split('tagged with ', 1)
		tag3 = tag2.pop()
		if tag3 not in common_tags:
			common_tags.append(tag3)
	return common_tags

######################################################
class AlumniHomePage(AbstractStudentHomePage):
	content_panels = AbstractStudentHomePage.content_panels + [
		InlinePanel('distinguished_alumni', label="Distinguished Alumni", max_num=10),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['AlumnusPage']
	max_count = 1

	def serve(self, request):
		alumni_list = self.get_children().live().order_by('alumnuspage__programme', 'alumnuspage__enrolment_year')

		all_interests = alumni_interests()
		# Filter by tag
		tag = request.GET.get('tag')
		if tag:
			alumni_list = alumni_list.filter(alumnuspage__interests__name=tag)
		paginator = Paginator(alumni_list, 10) # Show 10 alum per page
		page_no = request.GET.get('page_no')
		alumni_list = paginator.get_page(page_no)

		return render(request, self.template, {
			'page': self,
			'alumni_list': alumni_list,
			'all_interests':all_interests,
			'tag':tag,
			'page_no':page_no,
		})

	class Meta:
		verbose_name = "Alumni Home"

class AlumniInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'AlumnusPage',
		related_name='alumni_tagged_items',
		on_delete=models.CASCADE
	)

class AlumnusPage(AbstractStudentPage):
	user = models.OneToOneField(CustomUser, related_name='alumnus', null=True, on_delete=models.SET_NULL)
	contact_number_2 = models.CharField(max_length=20, blank=True)
	email_id_2 = models.EmailField(blank=True)
	address_line_1 = models.CharField(max_length=100, blank=True)
	address_line_2 = models.CharField(max_length=50, blank=True)
	address_line_3 = models.CharField(max_length=25, blank=True)
	interests = ClusterTaggableManager(through=AlumniInterestTag, blank=True, verbose_name='Interests')

	content_panels = Page.content_panels + [
		######################################################
		# The user should not be able to change these things from here
		FieldPanel('user'),
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('programme'),
		FieldPanel('roll_no'),
		FieldPanel('enrolment_year'),
		FieldPanel('email_id'), 
		######################################################
		FieldPanel('specialization'),
		FieldPanel('website'), 
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('contact_number'),
				FieldPanel('contact_number_2'),
			]),
		],  heading="Contact Numbers"),
		MultiFieldPanel([
			FieldPanel('address_line_1'),
			FieldPanel('address_line_2'),
			FieldPanel('address_line_3'),
		], heading="Current Address"),
		FieldPanel('hostel_address'),

		ImageChooserPanel('photo'), 
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('email_id_2'),
		InlinePanel('alum_gallery_images', label="Gallery images", max_num=5),
		InlinePanel('alum_links', label="Related Links", max_num=10),
		FieldPanel('interests'),
	]

	job_tab_panels = [
		InlinePanel('job_details', label="Job Details", max_num=3),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(job_tab_panels, heading="Job Details"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=['AlumniHomePage']
	subpage_types=[]

	class Meta:
		verbose_name = "Alumnus"
		verbose_name_plural = "Alumni"

class AlumnusPageJobDetail(Orderable):
	page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='job_details')
	title = models.CharField(max_length=20)
	company = models.CharField(max_length=20, blank=True)
	work_details = models.CharField(max_length=500, blank=True)
	link = models.URLField(max_length=250, blank=True)
	panels = [
		FieldPanel('title'),
		FieldPanel('company'),
		FieldPanel('work_details'),
		FieldPanel('link'),
	]

class AlumnusPageLink(Orderable):
	page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='alum_links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

class AlumnusPageGalleryImage(Orderable):
	page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='alum_gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('image'),
			FieldPanel('caption'),
		]),
	]

class DistinguishedAlumni(Orderable):
	page = ParentalKey(AlumniHomePage, on_delete=models.CASCADE, related_name='distinguished_alumni')
	distinguished_alumnus = models.ForeignKey('AlumnusPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='distinguished_alumnus')
	about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('distinguished_alumnus'),
		FieldPanel('about'),
	]

def alumni_interests():
	live_tags = AlumniInterestTag.objects.all()
	common_tags = []
	for tag in live_tags:
		tag2 = tag.__str__().split('tagged with ', 1)
		tag3 = tag2.pop()
		if tag3 not in common_tags:
			common_tags.append(tag3)
	return common_tags

# # How to make this function, student_interests() and faculty_interests() into one?
######################################################

@receiver(post_save, sender=CustomUser) #Can't use pre save cuz then user model won't be created and then the user onetoonekey field will raise error
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		if instance.user_type == '0':
			home = FacultyHomePage.objects.all()[0]  # Now be careful here as if there will be more than one facultyHomePage then there will be a problem

			base_slug = instance.username
			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			website='http://www.iitg.ac.in'
			new_faculty = FacultyPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=FacultyPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				website=website,
			)
			home.add_child(instance=new_faculty)
			home.save()
		elif instance.user_type == '1':
			home = StudentHomePage.objects.all()[0]
			base_slug = instance.username
			enrolment_year = datetime.strptime('Aug 1 20'+base_slug[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
			PROG = {'01':'0', '41':'1', '61':'2'}
			try:
				programme = PROG[base_slug[2:4]]
			except KeyError:
				programme = '3'

			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_student = StudentPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=StudentPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				roll_no=base_slug, #see some lines above
				enrolment_year=enrolment_year,
				programme=programme,
			)
			home.add_child(instance=new_student)
			home.save()
		elif instance.user_type == '2':
			home = AlumniHomePage.objects.all()[0]
			base_slug = instance.username
			enrolment_year = datetime.strptime('Aug 1 20'+base_slug[0:2]+' 12:00PM', '%b %d %Y %I:%M%p')
			PROG = {'01':'0', '41':'1', '61':'2'}
			try:
				programme = PROG[base_slug[2:4]]
			except KeyError:
				programme = '3'

			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_alum = AlumnusPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=AlumnusPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
				roll_no=base_slug, #see some lines above
				enrolment_year=enrolment_year,
				programme=programme,
			)
			home.add_child(instance=new_alum)
			home.save()
		elif instance.user_type == '3':
			home = StaffHomePage.objects.all()[0]
			base_slug = instance.username
			if not instance.email:
				mail_id=instance.username + "@iitg.ac.in"
			else:
				mail_id=instance.email
			new_staff = StaffPage(
				title= instance.first_name +" "+ instance.last_name,
				slug=StaffPage()._get_autogenerated_slug(base_slug),
				user=instance,
				first_name=instance.first_name,
				last_name=instance.last_name,
				email_id=mail_id,
			)
			home.add_child(instance=new_staff)
			home.save()
		else:
			pass

@receiver(pre_delete, sender=CustomUser)
def delete_user_profile(sender, instance, using, **kwargs):
	""" What happens when a user is deleted"""
	pass
######################################################
class ResearchHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[5])
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		InlinePanel('featured_research', label="Featured Research", max_num=10),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['ResearchLabPage', 'PublicationHomePage', 'ProjectHomePage']
	max_count = 1

	def serve(self, request):
		lab_list = self.get_children().live().order_by('researchlabpage__lab_type', 'researchlabpage__lab_research_area', 'researchlabpage__name')

		# Filter by research area
		area = request.GET.get('area')
		if area in ['0','1', '2', '3']:
			lab_list = lab_list.filter(researchlabpage__lab_research_area=area)
		ugpg = request.GET.get('ugpg')
		if ugpg in ['0','1']:
			lab_list = lab_list.filter(researchlabpage__lab_type=ugpg)

		return render(request, self.template, {
			'page': self,
			'lab_list': lab_list,
			'ugpg':ugpg,
			'area':area,
		})

	class Meta:
		verbose_name = "Research Home"

class FeaturedResearch(Orderable):
	page = ParentalKey(ResearchHomePage, on_delete=models.CASCADE, related_name='featured_research')
	featured_research = models.ForeignKey('PublicationPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='featured_research')
	panels = [
		AutocompletePanel('featured_research'),
	]
#------------------------------------------
class ResearchLabPage(Page):
	name = models.CharField(max_length=100)
	lab_type = models.CharField(max_length=2, choices=LAB_TYPES, default='0')
	lab_research_area = models.CharField(max_length=2, choices=LAB_RESEARCH_AREAS, default='0')
	# When already defined in faculty model who is lab incharge... then do we need it here?
	faculty_incharge = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_incharge')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	contact_number = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)
	photo_1 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_2 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_3 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('lab_type'),
		FieldPanel('lab_research_area'),
		FieldPanel('contact_number'),
		FieldPanel('address'),
		FieldPanel('intro'),
		FieldPanel('body'),
		MultiFieldPanel([
			FieldRowPanel([
				ImageChooserPanel('photo_1'),
				ImageChooserPanel('photo_2'),
				ImageChooserPanel('photo_3'),
			]),
		],  heading="Featured Photos"),
		InlinePanel('links', label="Related Links", max_num=10),
	]

	lab_equipment_panels = [
		InlinePanel('equipment', label="Lab Equipments", min_num=1),
	]

	people_panels = [
		AutocompletePanel('faculty_incharge'),
		InlinePanel('faculty', label="Faculty"),
		InlinePanel('students', label="Students"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(people_panels, heading="People"),
		ObjectList(lab_equipment_panels, heading="Equipments"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=['ResearchHomePage']
	subpage_types=[]

	class Meta:
		verbose_name = "Lab"
		verbose_name_plural = "Labs"

class LabEquipment(Orderable):
	name = models.CharField(max_length=25, blank=True)
	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='equipment')
	operator = models.ForeignKey('StaffPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='operator')
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	specifications = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	cost = models.FloatField(blank=True)
	date_of_procurement = models.DateField(blank=True)
	link = models.URLField(max_length=250, blank=True)
	photo_1 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	funding_agency = models.CharField(max_length=50, blank=True)
	funding_agency_link = models.URLField(max_length=250, blank=True)
	panels = [
		FieldPanel('name'),
		AutocompletePanel('operator'),
		DocumentChooserPanel('document'),
		FieldPanel('specifications'),
		FieldPanel('link'),
		FieldPanel('cost'),
		FieldPanel('date_of_procurement'),
		ImageChooserPanel('photo_1'), 
		MultiFieldPanel([
			FieldPanel('funding_agency'),
			FieldPanel('funding_agency_link'),

		], heading="Funding Agency"),
	]

class ResearchLabPageLink(Orderable):
	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

class ResearchLabFaculty(Orderable):
	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_lab')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('faculty'),
		FieldPanel('research_statement'),
	]

class ResearchLabStudents(Orderable):
	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_lab')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('student'),
		FieldPanel('research_statement'),
	]

#------------------------------------------
class PublicationHomePage(Page):
	# Add featured publications
	parent_page_types=['ResearchHomePage']
	subpage_types=['PublicationPage']
	max_count = 1

	class Meta:
		verbose_name = "Publication Home"

class PublicationPage(Page):
	#page = ParentalKey(PublicationHomePage, on_delete=models.PROTECT, related_name='publication')
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	name = models.CharField(max_length=100, blank=True)
	abstract = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	pub_type = models.CharField(max_length=2, choices=PUBLICATION_TYPES, default='0')
	download_link = models.URLField(blank=True, max_length=100)

	content_panels =  Page.content_panels + [
		DocumentChooserPanel('document'),
		FieldPanel('name'),
		FieldPanel('pub_type'),
		FieldPanel('abstract'),
		FieldPanel('download_link'),
		InlinePanel('images', label="Images", max_num=2),
		InlinePanel('links', label="Links", max_num=10),
	]

	people_panels = [
		InlinePanel('faculty', label="Faculty"),
		InlinePanel('students', label="Students"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(people_panels, heading="People"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=['PublicationHomePage']
	subpage_types=[ ]	

	class Meta:
		verbose_name = "Publication"
		verbose_name_plural = "Publications"

class PublicationPageStudent(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_pub')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('student'),
		FieldPanel('research_statement'),
	]

class PublicationPageFaculty(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_pub')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('faculty'),
		FieldPanel('research_statement'),
	]

class PublicationPageGalleryImage(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='images')
	photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('photo'),
			FieldPanel('caption'),
		]),
	]

#Is this going to be useful?
class PublicationPageLink(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

#------------------------------------------
class ProjectHomePage(Page):
	parent_page_types=['ResearchHomePage']
	subpage_types=['ProjectPage']
	max_count = 1

	class Meta:
		verbose_name = "Project Home"

class ProjectPage(Page):
	principal_investigator = models.ForeignKey('FacultyPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='principal_investigator')
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	name = models.CharField(max_length=100)
	start_date = models.DateField(default=timezone.now)
	end_date = models.DateField(blank=True)
	budget = models.FloatField(blank=True)
	funding_agency = models.CharField(max_length=100)
	funding_agency_link = models.URLField(blank=True, max_length=100)
	project_type = models.CharField(max_length=20, default='1', choices=PROJECT_TYPES)
	content_panels = Page.content_panels + [
		FieldPanel('project_type'),
		FieldPanel('name'),
		FieldPanel('description'),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('start_date'),
				FieldPanel('end_date'),
			]),
		],  heading="Duration"),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('funding_agency'),
				FieldPanel('funding_agency_link'),
				FieldPanel('budget'),
			]),
		],  heading="Funding details"),
		InlinePanel('links', label="Links", max_num=10),
		InlinePanel('gallery_images', label="Gallery images", max_num=3),
	]

	people_panels = [
		AutocompletePanel('principal_investigator'),
		InlinePanel('faculty', label="Faculty"),
		InlinePanel('students', label="Students"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(people_panels, heading="People"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=['ProjectHomePage']
	subpage_types=[ ]

	class Meta:
		verbose_name = "Project"
		verbose_name_plural = "Projects"

class ProjectPageFaculty(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('faculty'),
		FieldPanel('project_statement'),
	]

class ProjectPageStudent(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('student'),
		FieldPanel('project_statement'),
	]

class ProjectPageLink(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

class ProjectPageGalleryImage(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		FieldRowPanel([
			ImageChooserPanel('image'),
			FieldPanel('caption'),
		]),
	]	

#####################################################
class CourseStructure(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[6])

	intro = RichTextField(blank=True)
	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		InlinePanel('featured_courses', label="Featured Courses", max_num=10),
	]
	parent_page_types=['MechHomePage']
	subpage_types=['CoursePage']
	max_count = 1

	def serve(self, request):
		course_list = self.get_children().live().order_by('coursepage__name', 'coursepage__eligible_programmes', 'coursepage__semester')

		# structure = sem1 + sem2 + sem3 + sem4 + sem5 + sem6 + sem7 + sem8

		# Filter by department
		prog = request.GET.get('prog')
		if prog in ['0','1', '2', '3']:
			course_list = course_list.filter(coursepage__eligible_programmes=prog)

		structure = []
		sem1 = course_list.filter(coursepage__semester=1)
		structure.append(sem1)
		sem2 = course_list.filter(coursepage__semester=2)
		structure.append(sem2)
		sem3 = course_list.filter(coursepage__semester=3)
		structure.append(sem3)
		sem4 = course_list.filter(coursepage__semester=4)
		structure.append(sem4)
		sem5 = course_list.filter(coursepage__semester=5)
		structure.append(sem5)
		sem6 = course_list.filter(coursepage__semester=6)
		structure.append(sem6)
		sem7 = course_list.filter(coursepage__semester=7)
		structure.append(sem7)
		sem8 = course_list.filter(coursepage__semester=8)
		structure.append(sem8)

		return render(request, self.template, {
			'page': self,
			'course_list': course_list,
			'prog':prog,
			'structure':structure,
		})

	class Meta:
		verbose_name = "Course Structure"
		verbose_name_plural = "CourseStructure"

class CoursePage(Page):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	lectures = models.IntegerField(verbose_name="L")
	tutorials = models.IntegerField(verbose_name="T")
	practicals = models.IntegerField(verbose_name="P")
	credits = models.IntegerField(verbose_name="C")
	semester = models.IntegerField()
	course_type = models.CharField(max_length=100, choices=COURSE_TYPES, default='0')
	eligible_programmes = models.CharField(max_length=100, choices=STUDENT_PROGRAMME, default='0', help_text="Minimum qualification needed to take course")
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	course_page_link = models.URLField()
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)	#if can add function to add multiple students at once, then and only then add this.
	# list_of_students =

	content_panels =  Page.content_panels + [
		FieldPanel('name'),
		MultiFieldPanel([
			FieldPanel('code'),
			FieldPanel('semester'),
			FieldPanel('course_type'),
			FieldPanel('eligible_programmes'),
			FieldRowPanel([
				FieldPanel('lectures'),
				FieldPanel('tutorials'),
				FieldPanel('practicals'),
				FieldPanel('credits'),
			]),
			DocumentChooserPanel('document'),
			FieldPanel('course_page_link'),
		], heading="Course Details"),
		FieldPanel('description'),
		ImageChooserPanel('photo'),
		InlinePanel('course_instructor', label="Course Instructor", min_num=1),

	]

	announcement_tab_panels = [
		InlinePanel('course_announcements', label="Announcement"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(announcement_tab_panels, heading="Announcements"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=['CourseStructure']
	subpage_types=[ ]

	class Meta:
		verbose_name = "Course"
		verbose_name_plural = "Courses"

class CoursePageFaculty(Orderable):
	page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='course_instructor')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='course_instructor')
	session = models.DateField(verbose_name="Instruction start date", default=timezone.now)
	introduction = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		AutocompletePanel('faculty'),
		FieldPanel('introduction'),
		FieldPanel('session'),
	]

class CourseAnnouncementPage(Orderable):
	page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='course_announcements')
	announcement = RichTextField(max_length=250, blank=True, features=CUSTOM_RICHTEXT)
	document = models.ForeignKey(
		'wagtaildocs.Document',
		null=True, blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	panels = [
		FieldPanel('announcement'),
		DocumentChooserPanel('document'),
	]

class FeaturedCourse(Orderable):
	page = ParentalKey(CourseStructure, on_delete=models.CASCADE, related_name='featured_courses')
	featured_course = models.ForeignKey('CoursePage', null=True,blank=True, on_delete=models.SET_NULL, related_name='featured_course')
	panels = [
		AutocompletePanel('featured_course'),
	]
######################################################
class AwardHomePage(Page):
	parent_page_types=['MechHomePage']
	subpage_types=[]
	max_count = 1

	def serve(self, request):
		award_list = FacultyAward.objects.all()

		# Filter by research area
		award_type = request.GET.get('award_type')
		if award_type in ['0','1', '2']:
			award_list = award_list.filter(award_type=award_type)

		return render(request, self.template, {
			'page': self,
			'award_list': award_list,
			'award_type':award_type,
		})
	
	class Meta:
		verbose_name = "Awards Home"

	





