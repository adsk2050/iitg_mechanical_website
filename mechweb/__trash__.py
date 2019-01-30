########################## Uncommitted changes! Not sure to add! Look at it later ############
class EventHomePage(Page):
	# featured_event = models.ForeignKey('EventPage', on_delete=models.SET_NULL, related_name='featured_event')
	# content_panels = Page.content_panels + [
 #        InlinePanel('featured_event', label="Featured Event"),
 #    ]

	def get_context(self, request):
	    # Update context to include only published posts, ordered by reverse-chron
	    context = super().get_context(request)
	    navlist = self.get_children().live().order_by('-first_published_at')
	    context['event_list'] = event_list
	    return context

class EventPage(models.Model, Orderable):
    page = ParentalKey(EventHomePage, on_delete=models.CASCADE, related_name='event_page')

    event_name = models.CharField(blank=True, max_length=50)
    description = RichTextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(blank=True, max_length=50, choices=LOCATIONS, default='seminar_hall')
    poster = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
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

###################################################################


