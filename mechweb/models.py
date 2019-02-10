
from django.db import models
from django import forms

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  PageChooserPanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.images.edit_handlers import ImageChooserPanel
# for tagging
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS, EVENTS, FACULTY_DESIGNATION, STUDENT_PROGRAMME, STAFF_DESIGNATION

######################################################

#Need to work on how URLs work in wagtail. Can't access the pages !!!

######################################################
class MechHomePage(Page):
	intro = RichTextField(blank=True) 

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full"),
		InlinePanel('text_panels', label="Mini Articles"),
		InlinePanel('gallery_images', label="Gallery Images"),
	]

	parent_page_types=[]
	subpage_types=['EventHomePage', 'FacultyHomePage', 'StudentHomePage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		navlist = self.get_children().live().order_by('-first_published_at')
		context['navlist'] = navlist
		return context

class HomeTextPanel(Orderable):
	page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='text_panels')
	title = models.CharField(blank=True, max_length=50)
	description = models.CharField(blank=True, max_length=500)
	date = models.DateTimeField()
	#change the below content_type code to manage css accordingly
	content_type=models.CharField(
		default="mini_article", 
		choices=TEXT_PANEL_CONTENT_TYPES, 
		max_length=50
	)
	panels = [
		FieldPanel('title'),
		FieldPanel('description'),
		FieldPanel('date'),
		FieldPanel('content_type'),
	]

class MechHomePageGalleryImage(Orderable):
	page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]

######################################################
class EventHomePage(Page):
	featured_event = models.ForeignKey(
		'EventPage', 
		null=True,
		blank=True, 
		on_delete=models.SET_NULL, 
		related_name='featured_event'
	)
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
			FieldPanel('intro'),
			PageChooserPanel('featured_event'),
			#InlinePanel('event_page', label="New Event"),
		]

	parent_page_types=['MechHomePage']
	subpage_types=['EventPage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		event_list = self.get_children().live().order_by('-first_published_at')
		context['event_list'] = event_list
		return context

class EventPage(Page):
	# page = ParentalKey(EventHomePage, on_delete=models.PROTECT, related_name='event_page')

	event_name = models.CharField(blank=True, max_length=50)
	description = RichTextField(blank=True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	venue = models.CharField(blank=True, max_length=50, choices=LOCATIONS, default='seminar_hall')
	poster = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	document = models.ForeignKey(
		'wagtaildocs.Document', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
	)
	event_type = models.CharField(max_length=50, choices=EVENTS, default='meeting')
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
class FacultyHomePage(Page):	
	intro = RichTextField(blank=True)
	# head_of_dept = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='head_of_hept')

	content_panels = Page.content_panels + [
			FieldPanel('intro'),
			# PageChooserPanel('head_of_dept'),
			#InlinePanel('event_page', label="New Event"),
		]

	parent_page_types=['MechHomePage']
	subpage_types=['FacultyPage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		faculty_list = self.get_children().live().order_by('designation')
		context['faculty_list'] = faculty_list
		return context

class FacultyResearchInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'FacultyPage', 
		related_name='tagged_items', 
		on_delete=models.CASCADE )

class FacultyPage(Page):
	name = models.CharField(max_length=100)
	office_contact_number = models.CharField(max_length=20, blank=True)
	home_contact_number = models.CharField(max_length=20, blank=True)
	office_address_line_1 = models.CharField(max_length=25, blank=True)
	office_address_line_2 = models.CharField(max_length=50, blank=True)
	office_address_line_3 = models.CharField(max_length=100, blank=True)
	home_address_line_1 = models.CharField(max_length=25, blank=True)
	home_address_line_2 = models.CharField(max_length=50, blank=True)
	home_address_line_3 = models.CharField(max_length=100, blank=True)
	email_id = models.EmailField()
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True)
	research_interests = ClusterTaggableManager(through=FacultyResearchInterestTag, blank=True, verbose_name='Research Interests')
	joining_date = models.DateField()
	designation = models.CharField(max_length=25, choices=FACULTY_DESIGNATION, default='Assistant_Professor')
	website = models.URLField(max_length=250, null=True)
	# additional_roles = models.CharField(max_length=25, choices=FACULTY_ROLES, default='Assistant_Professor')
	#students
	#labs
	#projects

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('joining_date'),
		FieldPanel('designation'),
		# FieldPanel('additional_roles'),
		ImageChooserPanel('photo'),	
		FieldPanel('email_id'),	
		FieldPanel('website'),	
		MultiFieldPanel([
			FieldPanel('office_address_line_1'),
			FieldPanel('office_address_line_2'),
			FieldPanel('office_address_line_3'),
			FieldPanel('office_contact_number'),

		], heading="Office Address"),
		MultiFieldPanel([
			FieldPanel('home_address_line_1'),
			FieldPanel('home_address_line_2'),
			FieldPanel('home_address_line_3'),
			FieldPanel('home_contact_number'),
		], heading="Residence Address"),
		FieldPanel('intro'),
		FieldPanel('body'),
		InlinePanel('publications', label="Publications"),
		FieldPanel('research_interests'),
		InlinePanel('gallery_images', label="Gallery images"),
		InlinePanel('links', label="Related Links"),
		
	]

	parent_page_types=['FacultyHomePage']
	subpage_types=[]

	# def get_context(self, request):
	# 	# Filter by tag
	# 	tag = request.GET.get('tag')
	# 	blogpages = BlogPage.objects.filter(tags__name=tag)

	# 	# Update template context
	# 	context = super().get_context(request)
	# 	context['blogpages'] = blogpages
	# 	return context

class FacultyPublicationDocument(Orderable):
	page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='publications')
	document = models.ForeignKey(
		'wagtaildocs.Document', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
	)
	abstract = RichTextField(blank=True)
	link = models.URLField(max_length=250, blank=True)
	panels = [
		DocumentChooserPanel('document'),
		FieldPanel('abstract'),
		# FieldPanel('link'),
	]

class FacultyPageLink(Orderable):
	page = ParentalKey(FacultyPage, on_delete=models.CASCADE, related_name='links')
	link = models.URLField(max_length=250)
	panels = [
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

######################################################
class StudentHomePage(Page):  
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StudentPage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		student_list = self.get_children().live().order_by('programme').order_by('enrolment_year')
		context['student_list'] = student_list
		return context

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
	hostel_address_line_2 = models.CharField(max_length=50, blank=True)
	hostel_address_line_3 = models.CharField(max_length=100, blank=True)
	email_id = models.EmailField()
	enrolment_year = models.DateField()
	programme = models.CharField(max_length=25, choices=STUDENT_PROGRAMME, default='Bachelor')
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True)
	research_interests = ClusterTaggableManager(through=StudentResearchInterestTag, blank=True, verbose_name='Research Interests')
	website = models.URLField(max_length=250, null=True)
	faculty_advisor = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_advisor')

	content_panels = Page.content_panels + [
		FieldPanel('name'),
		FieldPanel('enrolment_year'),
		ImageChooserPanel('photo'), 
		FieldPanel('email_id'), 
		FieldPanel('contact_number'),
		MultiFieldPanel([
			FieldPanel('hostel_address_line_1'),
			FieldPanel('hostel_address_line_2'),
			FieldPanel('hostel_address_line_3'),
		], heading="Address"),
		FieldPanel('intro'),
		FieldPanel('body'),
		PageChooserPanel('faculty_advisor'),#shouldn't this be with faculty, so that studen't can't change faculty advisor by their own.
		InlinePanel('projects', label="Projects"),
		FieldPanel('research_interests'),
		InlinePanel('gallery_images', label="Gallery images"),
		InlinePanel('links', label="Related Links"),
	]

	parent_page_types=['StudentHomePage']
	subpage_types=[]

class StudentProject(Orderable):
	page = ParentalKey(StudentPage, on_delete=models.CASCADE, related_name='projects')
	guide = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='guide')
	co_guide = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='co_guide')
	document = models.ForeignKey(
		'wagtaildocs.Document', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
	)
	photo_1 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_2 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	photo_3 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	abstract = RichTextField(blank=True)
	link = models.URLField(max_length=250, blank=True)
	panels = [

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

######################################################
class StaffHomePage(Page):  
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['StaffPage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		staff_list = self.get_children().live().order_by('designation').order_by('joining_year')
		context['staff_list'] = staff_list
		return context

class StaffPage(Page):
	name = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)
	email_id = models.EmailField()
	joining_year = models.DateField()
	designation = models.CharField(max_length=25, choices=STAFF_DESIGNATION, default='Project_Staff')
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
		FieldPanel('address'),
		FieldPanel('intro'),
	]

	parent_page_types=['StaffHomePage']
	subpage_types=[]

######################################################
# class ResearchHomePage(Page):
# 	pass

# class ResearchLabPage(Page):
# 	name = models.CharField(max_length=100)
# 	pass