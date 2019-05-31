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
