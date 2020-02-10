class AcademicsHomePage(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		InlinePanel('featured_courses', label="Featured Courses", max_num=10),
	]
	parent_page_types=['MechHomePage']
	subpage_types=['CoursePage', 'CourseStructure']
	max_count = 1

class CourseStructure(Page):
	intro = RichTextField(blank=True, features=CUSTOM_RICHTEXT)
	programme = models.CharField(max_length=50, default='B.Tech')
	start_year = models.DateField(default=timezone.now)
	end_year = models.DateField(default=timezone.now)
	body = StreamField([
		()
	])