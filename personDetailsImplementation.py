# https://docs.djangoproject.com/en/2.2/topics/db/models/#abstract-base-classes

class PersonHomePage(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)

	content_panels = Page.content_panels + [
			FieldPanel('intro'),
		]

	parent_page_types=['MechHomePage']
	max_count = 1

	class Meta:
        abstract = True

	# This function is not working here
	# def list_common_interests(self):

	def serve(self, request):
		# Get faculty page models https://docs.wagtail.io/en/v2.2.2/reference/pages/model_recipes.html#tagging
		# Used the same method in student and alumni home pages
		person_list = self.get_children().live()
		all_interests = person_interests()

		# Filter by tag
		tag = request.GET.get('tag')
		if tag:
			person_list = person_list.filter(personpage__interests__name=tag)
				
		paginator = Paginator(person_list, 1) # Show 10 persons per page
		page_no = request.GET.get('page_no')
		person_list = paginator.get_page(page_no)

		return render(request, self.template, {
			'page': self,
			'person_list': person_list,
			'all_interests': all_interests,
			'tag':tag,
			'page_no':page_no,
		})

	# For staff we can add skill list rather than research interests.
	# This way we won't have to keep them separate
	
class PersonInterestTag(TaggedItemBase):
	content_object = ParentalKey(
		'PersonPage',
		related_name='tagged_items',
		on_delete=models.CASCADE )

	def person_interests(self):
		live_tags = self.objects.all()
		common_tags = []
		for tag in live_tags:
			tag2 = tag.__str__().split('tagged with ', 1)
			tag3 = tag2.pop()
			if tag3 not in common_tags:
				common_tags.append(tag3)
		return common_tags

	class Meta:
        abstract = True

class PersonPage(Page):
	user = models.OneToOneField(CustomUser, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_id = models.EmailField(unique=True)

	photo = models.ForeignKey('wagtailimages.Image',null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
	joining_date = models.DateField(default=timezone.now)
	leaving_date = models.DateField(blank=True, null=True)
	intro = models.CharField(max_length=250, blank=True)
	body = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	contact_number = models.CharField(max_length=20, blank=True)
	website = models.URLField(max_length=250, blank=True)
	address = models.CharField(max_length=250, blank=True)
	interests = ClusterTaggableManager(through=PersonInterestTag, blank=True, verbose_name='Interests')


	content_panels = Page.content_panels + [
		FieldPanel('user'),
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('email_id'), 

		ImageChooserPanel('photo'), 
		FieldPanel('joining_date'),
		FieldPanel('leaving_date'),
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('contact_number'),
		FieldPanel('website'),
		FieldPanel('address'),
		FieldPanel('interests'),
		InlinePanel('gallery_images', label="Gallery images"),
	]

	def __str__(self):
		return self.first_name+" "+self.last_name

	class Meta:
        abstract = True

class PersonPageGalleryImage(Orderable):
	page = ParentalKey(PersonPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey( 'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' )
	caption = models.CharField(blank=True, max_length=250)
	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]

	class Meta:
        abstract = True

######################################################

class FacultyHomePage(PersonHomePage):
	subpage_types=['FacultyPage']

class FacultyInterestTag(PersonInterestTag):

class FacultyPage(PersonPage):
	home_contact_number = models.CharField(max_length=20, blank=True)
	home_address = models.CharField(max_length=25, blank=True)
	designation = models.CharField(max_length=2, choices=FACULTY_DESIGNATION, default='3')
	#################################################################

	additional_roles = models.CharField(max_length=2, choices=FACULTY_ROLES, default='2')
	disposal_committee = models.CharField(max_length=2, choices=DISPOSAL_COMMITTEE, default='4')
	laboratory_in_charge = models.CharField(max_length=2, choices=LABORATORY_IN_CHARGE, default='14')
	faculty_in_charge = models.CharField(max_length=2, choices=FACULTY_IN_CHARGE, default='11')
	disciplinary_committee = models.CharField(max_length=2, choices=DISCIPLINARY_COMMITTEE, default='4')
	dupc = models.CharField(max_length=2, choices=DUPC, default='6')
	dppc = models.CharField(max_length=2, choices=DPPC, default='6')

	#################################################################
	content_panels = PersonPage.content_panels + [
		FieldPanel('designation'),
		MultiFieldPanel([
			FieldPanel('home_address_line_1'),
			FieldPanel('home_contact_number'),
		], heading="Residence Address"),
		# InlinePanel('publications', label="Publications"),
	]
	admin_role_panels = [
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
		ObjectList(admin_role_panels, heading="Administration"),
		ObjectList(announcement_tab_panels, heading="Announcement"),
		ObjectList(PersonPage.promote_panels, heading="Promote"),
		ObjectList(PersonPage.settings_panels, heading="Settings"),
	])


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

class FacultyPageGalleryImage(PersonPageGalleryImage):
	pass

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

######################################################
class StudentHomePage(PersonHomePage):
	subpage_types=['StudentPage']

class StudentPage(PersonPage):
	programme = models.CharField(max_length=2, choices=STUDENT_PROGRAMME)
	roll_no = models.IntegerField(default=160103001)
	faculty_advisor = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='faculty_advisor')

	content_panels = PersonPage.content_panels + [
		FieldPanel('programme'),
		FieldPanel('roll_no'),
		PageChooserPanel('faculty_advisor'),#shouldn't this be with faculty, so that studen't can't change faculty advisor by their own.
		InlinePanel('links', label="Related Links"),
	]
	project_tab_panels = [
		InlinePanel('projects', label="Projects"),
	]

	edit_handler = TabbedInterface([
		ObjectList(content_panels, heading="Content"),
		ObjectList(project_tab_panels, heading="Projects"),
		ObjectList(PersonPage.promote_panels, heading="Promote"),
		ObjectList(PersonPage.settings_panels, heading="Settings"),
	])

	parent_page_types=['StudentHomePage']
	subpage_types=[]

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

######################################################

class AlumniHomePage(PersonHomePage):
	content_panels = PersonHomePage.content_panels + [
		InlinePanel('distinguished_alumni', label="Distinguished Alumni"),
	]
	subpage_types=['AlumnusPage']

class DistinguishedAlumni(Orderable):
	page = ParentalKey(AlumniHomePage, on_delete=models.CASCADE, related_name='distinguished_alumni')
	distinguished_alumnus = models.ForeignKey('AlumnusPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='distinguished_alumnus')
	about = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	panels = [
		PageChooserPanel('distinguished_alumnus'),
		FieldPanel('about'),
	]

class AlumnusPage(StudentPage):
	#alum_as_student = models.ForeignKey('StudentPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='alum_as_student')
	contact_number_2 = models.CharField(max_length=20, blank=True)
	email_id_2 = models.EmailField()

	content_panels = StudentPage.content_panels + [
		FieldPanel('email_id_2'),
		FieldPanel('contact_number_2'),
		InlinePanel('job_details', label="Job Details"),
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

######################################################

class StaffHomePage(PersonHomePage):
	subpage_types=['StaffPage']
	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		staff_list = self.get_children().live().order_by('-first_published_at')
		context['staff_list'] = staff_list
		return context

class StaffPage(PersonPage):
	designation = models.CharField(max_length=25, choices=STAFF_DESIGNATION, default='Project_Staff')
	#if lab staff:
	# lab = models.ForeignKey('ResearchLabPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='lab')

	content_panels = Page.content_panels + [
		FieldPanel('designation'),
	]

	parent_page_types=['StaffHomePage']
	subpage_types=[]


######################################################
