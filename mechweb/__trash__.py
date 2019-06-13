######################################################
######################################################
# http://docs.wagtail.io/en/v2.5.1/advanced_topics/images/custom_image_model.html

# class CustomImage(AbstractImage):
#     # Add any extra fields to image here

#     # eg. To add a caption field:
#     # caption = models.CharField(max_length=255, blank=True)

#     admin_form_fields = Image.admin_form_fields + (
#         # Then add the field names here to make them appear in the form:
#         # 'caption',
#     )

# class CustomRendition(AbstractRendition):
#     image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

#     class Meta:
#         unique_together = (
#             ('image', 'filter_spec', 'focal_point_key'),
#         )

######################################################
######################################################
# http://docs.wagtail.io/en/v2.5.1/advanced_topics/documents/custom_document_model.html

# class CustomDocument(AbstractDocument):
#     # Custom field example:
#     source = models.CharField(
#         max_length=255,
#         # This must be set to allow Wagtail to create a document instance
#         # on upload.
#         blank=True,
#         null=True
#     )

#     admin_form_fields = Document.admin_form_fields + (
#         # Add all custom fields names to make them appear in the form:
#         'source',
#     )
######################################################
######################################################


class Site(models.Model):
    hostname = models.CharField(verbose_name=_('hostname'), max_length=255, db_index=True)
    port = models.IntegerField(
        verbose_name=_('port'),
        default=80,
        help_text=_(
            "Set this to something other than 80 if you need a specific port number to appear in URLs"
            " (e.g. development on port 8000). Does not affect request handling (so port forwarding still works)."
        )
    )
    site_name = models.CharField(
        verbose_name=_('site name'),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Human-readable name for the site.")
    )
    root_page = models.ForeignKey('Page', verbose_name=_('root page'), related_name='sites_rooted_here', on_delete=models.CASCADE)
    is_default_site = models.BooleanField(
        verbose_name=_('is default site'),
        default=False,
        help_text=_(
            "If true, this site will handle requests for all other hostnames that do not have a site entry of their own"
        )
    )
















































{% if tag %}&tag={{ tag }}{% endif %}

    <!-- Intro -->
    <h2>Intro:</h2>
    <div>{{ page.specific.intro }}</div>
    <hr>
    <div>{{ page.specific.body|richtext }}</div>
    <hr>
    <h3>Details:</h3>
    <ul>
        <li>Contact number : {{ page.specific.contact_number }}</li>
        <li>Address : {{ page.specific.hostel_address_line_1 }}</li>
        <li>Email ID : {{ page.specific.email_id }}</li>
        <li>Enrolment Year: {{ page.specific.enrolment_year }}</li>
        <li>Programme : {{ page.specific.programme }}</li>
        <li>Roll Number : {{ page.specific.roll_no }}</li>
        <li><a href="{{ page.specific.website }}">Personal website</a></li>
    </ul>
    <hr>
    <h3>Faculty Advisor : <a href="{{ page.specific.faculty_advisor.url }}">{{ page.specific.faculty_advisor }}</a></h3>

    <div>Research Interests:
        {% for tag in page.specific.research_interests.all %}
            <a href="{{ page.get_parent.url }}?tag={{ tag }}">{{ tag }}</a> |
        {% endfor %}
    </div>
    <hr>

    <!-- I want to show projects as popups which come up and display when clicked -->
    <h2>Projects:</h2>
    <ul>
        {% for project in page.specific.projects.all %}
            <li>
                <h4>{{ project.title }}</h4>

                <div>{% image project.photo_1 fill-100x100 %}</div>
                <div>{% image project.photo_2 fill-100x100 %}</div>
                <div>{% image project.photo_3 fill-100x100 %}</div>

                <div>Guide : {{ project.guide}}</div>
                {% if project.co_guide %}
                    <div>Co-guide : {{ project.co_guide}}</div>
                {% endif %}
                <div>{{ project.document|truncatechars:10 }} <a href="{{ project.document.url }}">Download</a></div>
                <h5>Abstract: </h5>
                <div>{{ project.abstract|richtext }}</div>
                <div><a href="{{ project.link}}">Link</a></div>
            </li>
            
        {% endfor %}
    </ul>
    <hr>
    
    <h3>Images</h3>
    <ul>
        {% for pic in page.specific.gallery_images.all %}
            <li>{% image pic.image fill-100x100 %}</li>
        {% endfor %}
    </ul>
    <hr>

    <h3>Links</h3>
    <ul>
        {% for link in page.specific.links.all %}
            <li><a href="{{ link }}">{{ link|truncatechars:10 }}</a></li>
        {% endfor %}
    </ul>
    <hr>  

    <!-- Intro -->
    <h2>Intro:</h2>
    <!-- <div class="intro">{{ page.intro|richtext }}</div> -->
    <hr>
    <!-- Featured Event -->
    <!-- <div>
        <h2>Featured Course: <a href="{% pageurl page.featured_event %}">{{ page.featured_event.specific.event_name }}</a></h2>
        <div>{% image page.featured_event.specific.poster fill-320x240 %}</div>
        <div>The {{ page.featured_event.specific.event_type }} will be held from: {{ page.featured_event.specific.start_date }} to {{ page.featured_event.specific.end_date }} at {{ page.featured_event.specific.venue }} </div>   
        <hr>
    </div> -->



class ResearchHomePage(Page):
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel(intro),
	]
	
	parent_page_types=['MechHomePage']
	subpage_types=['ResearchLabPage', 'PublicationHomePage', 'ProjectHomePage']

#------------------------------------------
class ResearchLabPage(Page):
	name = models.CharField(max_length=100)
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
		PageChooserPanel('faculty_incharge'),
		FieldPanel('contact_number'),
		FieldPanel('address'),
		FieldPanel('intro'),
		FieldPanel('body'),
		InlinePanel('students', label="Students"),
		InlinePanel('equipment', label="Lab Equipments"),
		InlinePanel('links', label="Related Links"),
		MultiFieldPanel([
			ImageChooserPanel('photo_1'), 
			ImageChooserPanel('photo_2'), 
			ImageChooserPanel('photo_3'),
		], heading ="Featured Photos")
	]

	parent_page_types=['ResearchHomePage']
	subpage_types=[]

# class LabEquipment(Orderable):
# 	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='equipment')
# 	operator = models.ForeignKey('StaffPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='operator')
# 	document = models.ForeignKey(
# 		'wagtaildocs.Document', 
# 		null=True, blank=True, 
# 		on_delete=models.SET_NULL, 
# 		related_name='+'
# 	)
# 	description = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	specifications = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	cost = models.FloatField(blank=True)
# 	date_of_procurement = models.DateField(blank=True)
# 	link = models.URLField(max_length=250, blank=True)
# 	photo_1 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	photo_2 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	photo_3 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	photo_4 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	photo_5 = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	panels = [
# 		PageChooserPanel('operator'),
# 		DocumentChooserPanel('document'),
# 		FieldPanel('description'),
# 		FieldPanel('link'),
# 		FieldPanel('cost'),
# 		FieldPanel('date_of_procurement'),
# 		MultiFieldPanel([
# 			ImageChooserPanel('photo_1'), 
# 			ImageChooserPanel('photo_2'), 
# 			ImageChooserPanel('photo_3'),
# 			ImageChooserPanel('photo_4'),
# 			ImageChooserPanel('photo_5'),
# 		], heading ="Featured Photos")
		 
# 	]

# class ResearchLabPageLink(Orderable):
# 	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='links')
# 	link = models.URLField(max_length=250)
# 	panels = [
# 		FieldPanel('link'),
# 	]

# class ResearchLabStudents(Orderable):
# 	page = ParentalKey(ResearchLabPage, on_delete=models.CASCADE, related_name='students')
# 	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student')
# 	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	panels = [
# 		PageChooserPanel('student'),
# 		FieldPanel('research_statement'),
# 	]

#------------------------------------------
class PublicationHomePage(Page):
	content_panels = Page.content_panels + [
		#InlinePanel('publication')
	]

	parent_page_types=['ResearchHomePage']
	subpage_types=['PublicationPage']

# class PublicationPage(Page):
# 	#page = ParentalKey(PublicationHomePage, on_delete=models.PROTECT, related_name='publication')
# 	document = models.ForeignKey(
# 		'wagtaildocs.Document', 
# 		null=True, blank=True, 
# 		on_delete=models.SET_NULL, 
# 		related_name='+'
# 	)
# 	name = models.CharField(max_length=100, blank=True)
# 	abstract = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	# photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	# student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_pub')
# 	# faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_pub')

# 	content_panels =  Page.content_panels + [
# 		DocumentChooserPanel('document'),
# 		FieldPanel('name'),
# 		FieldPanel('abstract'),
# 		InlinePanel('images', label="Images"),
# 		# ImageChooserPanel('photo'),
# 		# PageChooserPanel('student'),
# 		# PageChooserPanel('faculty'),
# 		InlinePanel('faculty', label="Faculty"),
# 		InlinePanel('students', label="Students"),
# 		InlinePanel('links', label="Links"),	
# 	]

# class PublicationPageStudent(Orderable):
# 	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='students')
# 	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='student_pub')
# 	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	panels = [
# 		PageChooserPanel('student'),
# 		FieldPanel('research_statement'),
# 	]

# class PublicationPageFaculty(Orderable):
# 	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='faculty')
# 	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_pub')
# 	research_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	panels = [
# 		PageChooserPanel('faculty'),
# 		FieldPanel('research_statement'),
# 	]

# class PublicationPageGalleryImage(Orderable):
# 	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='images')
# 	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
# 	panels = [
# 		ImageChooserPanel('photo'),
# 	]

# class PublicationPageLink(Orderable):
# 	page = ParentalKey(PublicationPage, on_delete=models.CASCADE, related_name='links')
# 	link = models.URLField(max_length=250)
# 	panels = [
# 		FieldPanel('link'),
# 	]

#------------------------------------------
class ProjectHomePage(Page):
	parent_page_types=['ResearchHomePage']
	subpage_types=['ProjectPage']

# class ProjectPage(Page):
# 	principal_investigator = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='principal_investigator')
# 	name = models.CharField(max_length=100)
# 	start_date = models.DateField(blank=True)
# 	end_date = models.DateField(blank=True)
# 	budget = models.FloatField(blank=True)
# 	funding_agency = models.CharField(max_length=100)
# 	funding_agency_link = models.URLField(blank=True, max_length=100)
# 	project_type = models.CharField(max_length=20, default='Academic', choices=PROJECT_TYPE)
# 	content_panels = Page.content_panels + [
# 		FieldPanel('name'),
# 		PageChooserPanel('principal_investigator'),
# 		FieldPanel('project_type'),
# 		FieldPanel('budget'),
# 		FieldPanel('start_date'),
# 		FieldPanel('end_date'),
# 		FieldPanel('funding_agency'),
# 		FieldPanel('funding_agency_link'),
# 		InlinePanel('students', label="Students"),
# 		InlinePanel('faculty', label="Faculty"),
# 		InlinePanel('links', label="Links"),
# 		InlinePanel('gallery_images', label="Gallery images"),
# 	]

# class ProjectPageFaculty(Orderable):
# 	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='faculty')
# 	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
# 	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	panels = [
# 		PageChooserPanel('faculty'),
# 		FieldPanel('project_statement'),
# 	]

# class ProjectPageStudent(Orderable):
# 	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='students')
# 	student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_co_investigator')
# 	project_statement = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
# 	panels = [
# 		PageChooserPanel('student'),
# 		FieldPanel('project_statement'),
# 	]

# class ProjectPageLink(Orderable):
# 	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='links')
# 	link = models.URLField(max_length=250)
# 	panels = [
# 		FieldPanel('link'),
# 	]

# class ProjectPageGalleryImage(Orderable):
# 	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images')
# 	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
# 	caption = models.CharField(blank=True, max_length=250)
# 	panels = [
# 		ImageChooserPanel('image'),
# 		FieldPanel('caption'),
# 	]




student_home_page.html
research_home_page.html
course_structure.html
staff_home_page.html
alumni_home_page.html 


class AlumniHomePage(StudentHomePage):
	content_panels = StudentHomePage.content_panels + [
		InlinePanel('distinguished_alumni', label="Distinguished Alumni"),
	]

	parent_page_types=['MechHomePage']
	subpage_types=['AlumnusPage']

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		alumni_list = self.get_children().live().order_by('programme').order_by('enrolment_year')
		context['alumni_list'] = alumni_list
		return context

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
	programme = models.CharField(max_length=25, choices=STUDENT_PROGRAMME, default='Bachelor')
	roll_no = models.IntegerField(default=160103001)
	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True)
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
			FieldPanel('address_line_1'),
			FieldPanel('address_line_3'),
		], heading="Address"),
		FieldPanel('intro'),
		FieldPanel('programme'),
		FieldPanel('roll_no'),
		FieldPanel('body'),
		InlinePanel('job_details', label="Job Details"),
		FieldPanel('interests'),
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
	about = RichTextField()
	panels = [
		PageChooserPanel('distinguished_alumnus'),
		FieldPanel('about'),
	]
