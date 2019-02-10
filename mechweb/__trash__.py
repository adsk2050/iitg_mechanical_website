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


class DepartmentalCommities(Page):
  head_of_dept = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='Head_of_Dept')

  DPPC_Chairman = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_Chairman')
  DPPC_Secretary = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_Secretary')
  DPPC_Faculty_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_Faculty_Member')
  DPPC_External_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_External_Member')
  DPPC_PhD_Student_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_PhD_Student_Member')
  DPPC_MTech_Student_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DPPC_MTech_Student_Member')

  DUPC_Chairman = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_Chairman')
  DUPC_Secretary = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_Secretary')
  DUPC_Faculty_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_Faculty_Member')
  DUPC_External_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_External_Member')
  DUPC_3rd_year_BTech = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_3rd_year_BTech')
  DUPC_2nd_year_BTech = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DUPC_2nd_year_BTech')

  DISCIPLINARY_COMMITTEE_Chairman = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISCIPLINARY_COMMITTEE_Chairman')
  DISCIPLINARY_COMMITTEE_Secretary = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISCIPLINARY_COMMITTEE_Secretary')
  DISCIPLINARY_COMMITTEE_Member_Secretary = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISCIPLINARY_COMMITTEE_Member_Secretary')
  DISCIPLINARY_COMMITTEE_Student_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISCIPLINARY_COMMITTEE_Student_Member')

  FACULTY_IN_CHARGE_BTP_Co_ordinator = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_BTP_Co_ordinator')
  FACULTY_IN_CHARGE_MTP_Co_ordinator = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_MTP_Co_ordinator')
  FACULTY_IN_CHARGE_Central_Workshop = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Central_Workshop')
  FACULTY_IN_CHARGE_Library_Committee = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Library_Committee')
  FACULTY_IN_CHARGE_Training_and_Placement = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Training_and_Placement')
  FACULTY_IN_CHARGE_Departmental_Seminar_Room = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Departmental_Seminar_Room')
  FACULTY_IN_CHARGE_Secretary_Faculty_Meeting = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Secretary_Faculty_Meeting')
  FACULTY_IN_CHARGE_PG_Computational_Lab = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_PG_Computational_Lab')
  FACULTY_IN_CHARGE_Research_Scholar_Room = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Research_Scholar_Room')
  FACULTY_IN_CHARGE_Time_Table_Committee = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Time_Table_Committee')
  FACULTY_IN_CHARGE_Departmental_Website = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='FACULTY_IN_CHARGE_Departmental_Website')

  LABORATORY_IN_CHARGE_Advanced_Manufacturing_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Advanced_Manufacturing_Laboratory')
  LABORATORY_IN_CHARGE_CAD_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_CAD_Laboratory')
  LABORATORY_IN_CHARGE_Central_Workshop = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Central_Workshop')
  LABORATORY_IN_CHARGE_Fluid_Mechanics_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Fluid_Mechanics_Laboratory')
  LABORATORY_IN_CHARGE_IC_Engines_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_IC_Engines_Laboratory')
  LABORATORY_IN_CHARGE_Instrumentation_and_Control_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Instrumentation_and_Control_Laboratory')
  LABORATORY_IN_CHARGE_Material_Science_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Material_Science_Laboratory')
  LABORATORY_IN_CHARGE_Tribology_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Tribology_Laboratory')
  LABORATORY_IN_CHARGE_Mechatronics_and_Robotics_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Mechatronics_and_Robotics_Laboratory')
  LABORATORY_IN_CHARGE_Strength_of_Materials_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Strength_of_Materials_Laboratory')
  LABORATORY_IN_CHARGE_Theory_of_Machines_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Theory_of_Machines_Laboratory')
  LABORATORY_IN_CHARGE_Thermal_Science_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Thermal_Science_Laboratory')
  LABORATORY_IN_CHARGE_Turbo_Machinary_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Turbo_Machinary_Laboratory')
  LABORATORY_IN_CHARGE_Vibrations_and_Acoustics_Laboratory = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='LABORATORY_IN_CHARGE_Vibrations_and_Acoustics_Laboratory')

  DISPOSAL_COMMITTEE_Chairman = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISPOSAL_COMMITTEE_Chairman')
  DISPOSAL_COMMITTEE_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISPOSAL_COMMITTEE_Member')
  DISPOSAL_COMMITTEE_External_Member = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISPOSAL_COMMITTEE_External_Member')
  DISPOSAL_COMMITTEE_Non_Member_Secretary = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='DISPOSAL_COMMITTEE_Non_Member_Secretary')