class CourseStructure(Page):
	pass

class CoursePage(Page):
	title = models.CharField(max_length=50)
	code = models.CharField(max_length=10)
	lectures = models.IntegerField()
	tutorials = models.IntegerField()
	practicals = models.IntegerField()
	credits = models.IntegerField()
	semester = models.IntegerField()
	eligible_programmes = models.CharField(choices=STUDENT_PROGRAMME)
	description = models.RichTextField()
	course_page_link = 
	document = models.ForeignKey(
		'wagtaildocs.Document', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
	)	#if can add function to add multiple students at once, then and only then add this.
	list_of_students = 

	content_panels =  Page.content_panels + [
		FieldPanel('name'),
		DocumentChooserPanel('document'),
		FieldPanel('abstract'),
		ImageChooserPanel('photo'),
		# PageChooserPanel('student'),
		# PageChooserPanel('faculty'),
		InlinePanel('students', label="Students"),
		InlinePanel('faculty', label="Faculty"),
		InlinePanel('links', label="Links"),	
	]
	

class CoursePageFaculty(Orderable):
	page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='faculty')
	faculty = models.ForeignKey('FacultyPage', null=True,blank=True, on_delete=models.SET_NULL, related_name='course_instructor')
	introduction = RichTextField(blank=True)
	panels = [
		PageChooserPanel('faculty'),
		FieldPanel('introduction'),
	]

class CourseAnnouncementPage(Orderable):
	page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='links')
	announcement = models.RichTextField(max_length=250)
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