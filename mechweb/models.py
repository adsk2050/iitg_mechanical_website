
from django.db import models
from django import forms

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, FieldRowPanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

from .constants import TEXT_PANEL_CONTENT_TYPES, LOCATIONS


class MechHomePage(Page):
    intro = RichTextField(blank=True) 

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('text_panels', label="Mini Articles"),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]

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
    content_type=models.CharField(default="mini_article", choices=TEXT_PANEL_CONTENT_TYPES, max_length=50)
    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('date'),
        FieldPanel('content_type'),
    ]

class MechHomePageGalleryImage(Orderable):
    page = ParentalKey(MechHomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


