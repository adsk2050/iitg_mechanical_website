# delete existing root root_page
# create MechHomePage
# create site corresponding to MechHomePage by defining:
# 'hostname', 
# 'port', 
# 'site_name', 
# 'root_page', 
# 'is_default_site'

# create child pages of MechHomePage in the following order:
# Academics - course structure
# Research
# Awards
# Events
# Alumni
# Faculty
# Students
# Staff


from wagtail.core.models import Page, Site
from mechweb.models  import MechHomePage, EventHomePage, FacultyHomePage, StudentHomePage, StaffHomePage, AlumniHomePage, ResearchHomePage, ResearchLabHomePage, PublicationHomePage, ProjectHomePage, AwardHomePage, CourseStructure, Categories, CategoriesHome

# root = Page.objects.all()[0] # Need to verify if Root is always first object or not... dumb of course it will
pages = Page.objects.all()[1:]
for page in pages:
	page.delete()

root = Page.objects.get(path='0001')

home = MechHomePage(
	title= "Home|ME|IITG",
	slug="mech", # Assuming there are no slugs so no need to check if its available
	seo_title="Mechanical Engineering · IITG",
)
root.add_child(instance=home)
root.save()

sites = Site.objects.all()
for site in sites:
	site.delete()

home_site = Site(
	hostname='127.0.0.1', 
	port=8000, 
	site_name='Home', 
	root_page=home, 
	is_default_site=True,
)
home_site.save()

if CategoriesHome.objects.all().count()>0:
	for interestcategoryhomepage in CategoriesHome.objects.all():
		interestcategoryhomepage.delete()
if Categories.objects.all().count()>0:
	for interestcategory in Categories.objects.all():
		interestcategory.delete()
interestcateogryhome = CategoriesHome(
	title='Research Interest Categories',
	slug='research_interest_divisions',	
)
home.add_child(instance=interestcateogryhome)
home.save()
# interestcateogry0=Categories(
# 	title='Other',
# 	slug='others',
# 	category='0'
# )
# interestcateogryhome.add_child(instance=interestcateogry0)
# interestcateogryhome.save()
interestcateogry1=Categories(
	title='Machine Design Engineering',
	slug='machine_design',
	category='1'
)
interestcateogryhome.add_child(instance=interestcateogry1)
interestcateogryhome.save()
interestcateogry2=Categories(
	title='Manufacturing Engineering',
	slug='manufacturing',
	category='2'
)
interestcateogryhome.add_child(instance=interestcateogry2)
interestcateogryhome.save()
interestcateogry3=Categories(
	title='Thermal and Fluid Engineering',
	slug='thermal_and_fluid',
	category='3'
)
interestcateogryhome.add_child(instance=interestcateogry3)
interestcateogryhome.save()

# main pages after homepage:
academics_home_page = CourseStructure(
	title='Academics',
	slug='academics',
	seo_title="Academics | Mechanical Engineering · IITG",
)
home.add_child(instance=academics_home_page)
home.save()
research_home_page = ResearchHomePage(
	title='Research',
	slug='research',
	seo_title="Research | Mechanical Engineering · IITG",
)
home.add_child(instance=research_home_page)
home.save()
publication_home_page = PublicationHomePage(
	title='Publications',
	slug='publications',
	seo_title="Publications | Mechanical Engineering · IITG",
)
research_home_page.add_child(instance=publication_home_page)
research_home_page.save()

research_lab_home_page = ResearchLabHomePage(
	title='Facilities(Labs)',
	slug='facilities',
	seo_title="Facilities(Labs) | Mechanical Engineering · IITG",
)
research_home_page.add_child(instance=research_lab_home_page)
research_home_page.save()

#####################################################################
# research_lab_page = ResearchLabPage(
# 	title='Facilities(Labs)',
# 	slug='facilities',
# 	seo_title="Facilities(Labs) | Mechanical Engineering · IITG",
# 	name="",
# 	lab_type="",
# 	lab_research_area="",
# 	intro="",
# 	body="",
# 	contact_number="",
# 	address="",
# )
# research_lab_home_page.add_child(instance=research_lab_page)
# research_lab_home_page.save()

#####################################################################

project_home_page = ProjectHomePage(
	title='Projects',
	slug='projects',
	seo_title="Projects | Mechanical Engineering · IITG",
)
research_home_page.add_child(instance=project_home_page)
research_home_page.save()
faculty_home_page = FacultyHomePage(
	title='Faculty',
	slug='faculty',
	seo_title="Faculty | Mechanical Engineering  · IITG",
)
home.add_child(instance=faculty_home_page)
home.save()
student_home_page = StudentHomePage(
	title='Students',
	slug='students',
	seo_title="Students | Mechanical Engineering · IITG",
)
home.add_child(instance=student_home_page)
home.save()
staff_home_page = StaffHomePage(
	title='Staff',
	slug='staff',
	seo_title="Staff | Mechanical Engineering · IITG",
)
home.add_child(instance=staff_home_page)
home.save()
# alumni_home_page = AlumniHomePage(
# 	title='Alumni',
# 	slug='alumni',
# 	seo_title="Alumni | Mechanical Engineering · IITG",
# )
# home.add_child(instance=alumni_home_page)
# home.save()

award_home_page = AwardHomePage(
	title='Awards',
	slug='awards',
	seo_title="Awards | Mechanical Engineering · IITG",
)
home.add_child(instance=award_home_page)
home.save()
event_home_page = EventHomePage(
	title='Events',
	slug='events',
	seo_title="Events | Mechanical Engineering · IITG",
)
home.add_child(instance=event_home_page)
home.save()
































































































































































































































