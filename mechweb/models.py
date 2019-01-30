
from django.db import models
from django import forms

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,  PageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS, EVENTS

######################################################

class MechHomePage(Page):
	intro = RichTextField(blank=True) 

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full"),
		InlinePanel('text_panels', label="Mini Articles"),
		InlinePanel('gallery_images', label="Gallery Images"),
	]

	parent_page_types=[]
	subpage_types=['EventHomePage']

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

#######################################################

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

#######################################################





