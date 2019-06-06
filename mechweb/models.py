
from django.db import models
from django import forms
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  PageChooserPanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.images.edit_handlers import ImageChooserPanel
# for tagging
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag

from iitg_mechanical_website.settings.base import CUSTOM_RICHTEXT

from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS, EVENTS, STUDENT_PROGRAMME, STAFF_DESIGNATION, PROJECT_TYPES, PUBLICATION_TYPES, LAB_TYPES
# , NAV_ORDER

from .constants import DISPOSAL_COMMITTEE, LABORATORY_IN_CHARGE, FACULTY_IN_CHARGE, DISCIPLINARY_COMMITTEE, DUPC, DPPC,FACULTY_DESIGNATION, FACULTY_ROLES

######################################################

#Need to work on how URLs work in wagtail. Can't access the pages !!!

######################################################
class MechHomePage(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	# intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full"),
		# InlinePanel('text_panels', label="Mini Articles"),
		InlinePanel('gallery_images', label="Gallery Images"),
	]

	notification_tab_panels = [
		InlinePanel('text_panels', label="Mini Articles"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(notification_tab_panels, heading="News & Notifications"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	parent_page_types=[]
	subpage_types=['EventHomePage', 'FacultyHomePage', 'StudentHomePage', 'ResearchHomePage', 'StaffHomePage', 'CourseStructure', 'AlumniHomePage']

	max_count = 1

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		navlist = self.get_children().live().order_by('-first_published_at')
		context['navlist'] = navlist
		return context

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
		ImageChooserPanel('photo'),
		FieldPanel('caption'),
	]

######################################################
class EventHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[0])
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
			PageChooserPanel('featured_event'),
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

class EventPage(Page):
	# page = ParentalKey(EventHomePage, on_delete=models.PROTECT, related_name='event_page')

	event_name = models.CharField(blank=True, max_length=50)
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	start_date = models.DateTimeField()
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
		FieldPanel('event_name'),
		FieldPanel('description'),
		FieldPanel('start_date'),
		FieldPanel('end_date'),
		FieldPanel('venue'),
		ImageChooserPanel('poster'),
		# InlinePanel('poster', label="Poster"),
		DocumentChooserPanel('document'),
		FieldPanel('event_type'),
		InlinePanel('gallery_images', label="Gallery Images"),
		InlinePanel('links', label="Related Links"),
	]

	# promote_panels=[]
	# settings_panels=[]

	parent_page_types=['EventHomePage']
	subpage_types=[]

class EventPageGalleryImage(Orderable):
	page = ParentalKey(EventPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image',
		on_delete=models.CASCADE,
		related_name='+'
	)
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
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
		faculty_list = self.get_children().live().order_by('facultypage__name')

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

class FacultyResearchInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'FacultyPage',
		related_name='tagged_items',
		on_delete=models.CASCADE )
	# This function is working here only in shell but not during rendering
	# def list_common_interests(self):

class FacultyPage(Page):
	name = models.CharField(max_length=100)
	office_contact_number = models.CharField(max_length=20, blank=True)
	home_contact_number = models.CharField(max_length=20, blank=True)
	office_address_line_1 = models.CharField(max_length=25, blank=True)
	home_address_line_1 = models.CharField(max_length=25, blank=True)
	email_id = models.EmailField()
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	research_interests = ClusterTaggableManager(through=FacultyResearchInterestTag, blank=True, verbose_name='Research Interests')
	joining_date = models.DateField()
	leaving_date = models.DateField(blank=True, null=True)
	designation = models.CharField(max_length=2, choices=FACULTY_DESIGNATION, default='3')
	website = models.URLField(max_length=250, null=True)
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
		FieldPanel('name'),
		FieldPanel('joining_date'),
		FieldPanel('leaving_date'),
		FieldPanel('designation'),
		ImageChooserPanel('photo'),
		FieldPanel('email_id'),
		FieldPanel('website'),
		MultiFieldPanel([
			FieldPanel('office_address_line_1'),
			FieldPanel('office_contact_number'),

		], heading="Office Address"),
		MultiFieldPanel([
			FieldPanel('home_address_line_1'),
			FieldPanel('home_contact_number'),
		], heading="Residence Address"),
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('research_interests'),
		InlinePanel('gallery_images', label="Gallery images"),
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

	announcement_tab_panels = [
		InlinePanel('faculty_announcement', label="Announcement"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(custom_tab_panels, heading="Administration"),
		ObjectList(announcement_tab_panels, heading="Announcement"),
		ObjectList(Page.promote_panels, heading="Promote"),
		ObjectList(Page.settings_panels, heading="Settings"),
	])

	# Not working 
	# def faculty_labs(self):
	# 	lab_relation_list = self.faculty_lab.all()
	# 	lab_list = []
	# 	for lab_relation in lab_relation_list:
	# 		lab = lab.page
	# 		lab_list.append(lab)
	# 	return lab_list

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

		context = super().get_context(request)
		context['lab_list'] = lab_list
		context['pub_list'] = pub_list
		context['project_list'] = project_list
		return context


	parent_page_types=['FacultyHomePage']
	subpage_types=[]

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
		ImageChooserPanel('image'),
		FieldPanel('caption'),
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
class StudentHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[2])
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StudentPage']
	max_count = 1

	def serve(self, request):
		student_list = self.get_children().live().order_by('studentpage__name')
		# btech_student_list = student_list.filter(programme='0')
		# mtech_student_list = student_list.filter(programme='1')
		# phd_student_list = student_list.filter(programme='2')
		# postdoc_student_list = student_list.filter(programme='3')
		# https://docs.wagtail.io/en/v2.5.1/reference/contrib/modeladmin/indexview.html

		all_research_interests = student_interests()
		# Filter by tag
		tag = request.GET.get('tag')
		if tag:
			student_list = student_list.filter(studentpage__research_interests__name=tag)
		paginator = Paginator(student_list, 10) # Show 10 faculty per page
		page_no = request.GET.get('page_no')
		student_list = paginator.get_page(page_no)

		return render(request, self.template, {
			'page': self,
			'student_list': student_list,
			# 'btech_student_list': btech_student_list, 
			# 'mtech_student_list': mtech_student_list, 
			# 'phd_student_list': phd_student_list, 
			# 'postdoc_student_list': postdoc_student_list, 
			'all_research_interests': all_research_interests,
			'tag':tag,
			'page_no':page_no,
		})

class StudentResearchInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'StudentPage',
		related_name='tagged_items',
		on_delete=models.CASCADE
	)

class StudentPage(Page):
	name = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=20, blank=True)
	hostel_address_line_1 = models.CharField(max_length=25, blank=True)
	email_id = models.EmailField()
	enrolment_year = models.DateField()
	programme = models.CharField(max_length=2, choices=STUDENT_PROGRAMME, default='0')
	roll_no = models.IntegerField(default=160103001)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	research_interests = ClusterTaggableManager(through=StudentResearchInterestTag, blank=True, verbose_name='Research Interests')
	website = models.URLField(max_length=250, blank=True)
	faculty_advisor = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_advisor')

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('enrolment_year'),
		ImageChooserPanel('photo'), 
		FieldPanel('email_id'), 
		FieldPanel('website'), 
		FieldPanel('contact_number'),
		FieldPanel('hostel_address_line_1'),
		FieldPanel('intro'),
		FieldPanel('programme'),
		FieldPanel('roll_no'),
		FieldPanel('body'),
		PageChooserPanel('faculty_advisor'),#shouldn't this be with faculty, so that studen't can't change faculty advisor by their own.
		FieldPanel('research_interests'),
		InlinePanel('gallery_images', label="Gallery images"),
		InlinePanel('links', label="Related Links"),
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

	parent_page_types=['StudentHomePage']
	subpage_types=[]

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
		PageChooserPanel('guide'),
		PageChooserPanel('co_guide'),
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
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('link'),
	]

class StudentPageGalleryImage(Orderable):
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
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
class AlumniHomePage(StudentHomePage):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[3])
	content_panels = StudentHomePage.content_panels + [
		InlinePanel('distinguished_alumni', label="Distinguished Alumni"),
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
			new_template = 'mechweb/alumni_tag_page.html'
			alumni_list = alumni_list.filter(alumnuspage__interests__name=tag)
		paginator = Paginator(alumni_list, 10) # Show 10 faculty per page
		page_no = request.GET.get('page_no')
		alumni_list = paginator.get_page(page_no)

		return render(request, self.template, {
			'page': self,
			'alumni_list': alumni_list,
			'all_interests':all_interests,
			'tag':tag,
			'page_no':page_no,
		})

class AlumniInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'AlumnusPage',
		related_name='alumni_tagged_items',
		on_delete=models.CASCADE
	)

class AlumnusPage(Page):
	#alum_as_student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='alum_as_student')
	name = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=20, blank=True)
	contact_number_2 = models.CharField(max_length=20, blank=True)
	email_id = models.EmailField()
	email_id_2 = models.EmailField()
	address_line_1 = models.CharField(max_length=25, blank=True)
	address_line_2 = models.CharField(max_length=50, blank=True)
	address_line_3 = models.CharField(max_length=100, blank=True)
	enrolment_year = models.DateField()
	programme = models.CharField(max_length=2, choices=STUDENT_PROGRAMME, default='0')
	roll_no = models.IntegerField(default=160103001)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	interests = ClusterTaggableManager(through=AlumniInterestTag, blank=True, verbose_name='Interests')
	website = models.URLField(max_length=250, null=True)

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('enrolment_year'),
		ImageChooserPanel('photo'),
		FieldPanel('email_id'),
		FieldPanel('email_id_2'),
		FieldPanel('contact_number'),
		FieldPanel('contact_number_2'),
		MultiFieldPanel([
			FieldPanel('address_line_1'),
			FieldPanel('address_line_2'),
			FieldPanel('address_line_3'),
		], heading="Address"),
		FieldPanel('intro'),
		FieldPanel('programme'),
		FieldPanel('roll_no'),
		FieldPanel('description'),
		InlinePanel('job_details', label="Job Details"),
		FieldPanel('interests'),
		FieldPanel('website'),
	]

	parent_page_types=['AlumniHomePage']
	subpage_types=[]

class AlumnusPageJobDetail(Orderable):
	page = ParentalKey(AlumnusPage, on_delete=models.CASCADE, related_name='job_details')
	title = models.CharField(max_length=20, blank=True)
	company = models.CharField(max_length=20, blank=True)
	work_details = models.CharField(max_length=500, blank=True)
	link = models.URLField(max_length=250)
	panels = [
		FieldPanel('title'),
		FieldPanel('company'),
		FieldPanel('work_details'),
		FieldPanel('link'),
	]

class DistinguishedAlumni(Orderable):
	page = ParentalKey(AlumniHomePage, on_delete=models.CASCADE, related_name='distinguished_alumni')
	distinguished_alumnus = models.ForeignKey('AlumnusPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='distinguished_alumnus')
	about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('distinguished_alumnus'),
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

# How to make this function, student_interests() and faculty_interests() into one?

######################################################
class StaffHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[4])
	use_other_template = models.IntegerField(default = 3)#Find a way to remove this shit without deleting the original entry
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)


	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('use_other_template')
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StaffPage']
	max_count = 1

	# and this too
	def get_template(self,request):
		return 'mechweb/staff_home_page.html'

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		staff_list = self.get_children().live().order_by('-first_published_at')
		context['staff_list'] = staff_list
		return context

class StaffPage(Page):
	name = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)
	email_id = models.EmailField()
	joining_year = models.DateField()
	designation = models.CharField(max_length=2, choices=STAFF_DESIGNATION, default='1')
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	#if lab staff:
	# lab = models.ForeignKey('ResearchLabPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='lab')

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('joining_year'),
		ImageChooserPanel('photo'),
		FieldPanel('email_id'),
		FieldPanel('contact_number'),
		FieldPanel('designation'),
		FieldPanel('address'),
		FieldPanel('intro'),
	]

	parent_page_types=['StaffHomePage']
	subpage_types=[]

######################################################
class ResearchHomePage(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[5])
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['ResearchLabPage', 'PublicationHomePage', 'ProjectHomePage']
	max_count = 1

#------------------------------------------
class ResearchLabPage(Page):
	name = models.CharField(max_length=100)
	lab_type = models.CharField(max_length=2, choices=LAB_TYPES, default='0')
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
		PageChooserPanel('faculty_incharge'),
		FieldPanel('contact_number'),
		FieldPanel('address'),
		FieldPanel('intro'),
		FieldPanel('body'),
		InlinePanel('links', label="Related Links"),
		MultiFieldPanel([
			ImageChooserPanel('photo_1'),
			ImageChooserPanel('photo_2'),
			ImageChooserPanel('photo_3'),
		], heading ="Featured Photos")
	]

	lab_equipment_panels = [
		InlinePanel('equipment', label="Lab Equipments"),
	]

	people_panels = [
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
		PageChooserPanel('operator'),
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
		PageChooserPanel('faculty'),
		FieldPanel('research_statement'),
	]

class ResearchLabStudents(Orderable):
	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_lab')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('student'),
		FieldPanel('research_statement'),
	]

#------------------------------------------
class PublicationHomePage(Page):
	# Add featured publications
	parent_page_types=['ResearchHomePage']
	subpage_types=['PublicationPage']
	max_count = 1

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
	# photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	# student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_pub')
	# faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_pub')

	content_panels =  Page.content_panels + [
		DocumentChooserPanel('document'),
		FieldPanel('name'),
		FieldPanel('pub_type'),
		FieldPanel('abstract'),
		FieldPanel('download_link'),
		InlinePanel('images', label="Images"),
		# ImageChooserPanel('photo'),
		# PageChooserPanel('student'),
		# PageChooserPanel('faculty'),
		# InlinePanel('faculty', label="Faculty"),
		# InlinePanel('students', label="Students"),
		InlinePanel('links', label="Links"),
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

class PublicationPageStudent(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_pub')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('student'),
		FieldPanel('research_statement'),
	]

class PublicationPageFaculty(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_pub')
	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('faculty'),
		FieldPanel('research_statement'),
	]

class PublicationPageGalleryImage(Orderable):
	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='images')
	photo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		ImageChooserPanel('photo'),
		FieldPanel('caption'),
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

class ProjectPage(Page):
	principal_investigator = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='principal_investigator')
	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	name = models.CharField(max_length=100)
	start_date = models.DateField(blank=True)
	end_date = models.DateField(blank=True)
	budget = models.FloatField(blank=True)
	funding_agency = models.CharField(max_length=100)
	funding_agency_link = models.URLField(blank=True, max_length=100)
	project_type = models.CharField(max_length=20, default='1', choices=PROJECT_TYPES)
	content_panels = Page.content_panels + [
		FieldPanel('name'),
		PageChooserPanel('principal_investigator'),
		FieldPanel('description'),
		FieldPanel('project_type'),
		FieldPanel('budget'),
		FieldPanel('start_date'),
		FieldPanel('end_date'),
		FieldPanel('funding_agency'),
		FieldPanel('funding_agency_link'),
		InlinePanel('links', label="Links"),
		InlinePanel('gallery_images', label="Gallery images"),
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

class ProjectPageFaculty(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('faculty'),
		FieldPanel('project_statement'),
	]

class ProjectPageStudent(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='students')
	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('student'),
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
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]

######################################################
class CourseStructure(Page):
	#nav_order = models.CharField(max_length=1, default=NAV_ORDER[6])
	parent_page_types=['MechHomePage']
	subpage_types=['CoursePage']
	max_count = 1

class CoursePage(Page):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	lectures = models.IntegerField()
	tutorials = models.IntegerField()
	practicals = models.IntegerField()
	credits = models.IntegerField()
	semester = models.IntegerField()
	eligible_programmes = models.CharField(max_length=100, choices=STUDENT_PROGRAMME, default='0', verbose_name="Minimum qualification")
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
			FieldPanel('lectures'),
			FieldPanel('tutorials'),
			FieldPanel('practicals'),
			FieldPanel('credits'),
			DocumentChooserPanel('document'),
			FieldPanel('semester'),
			FieldPanel('eligible_programmes'),
			FieldPanel('course_page_link'),
		], heading="Course Details"),
		FieldPanel('description'),
		ImageChooserPanel('photo'),
		InlinePanel('course_instructor', label="Course Instructor"),

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

class CoursePageFaculty(Orderable):
	page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='course_instructor')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='course_instructor')
	introduction = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('faculty'),
		FieldPanel('introduction'),
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

######################################################
