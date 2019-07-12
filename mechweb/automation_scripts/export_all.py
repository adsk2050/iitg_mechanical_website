
from mechweb.admin import(CustomUserResource, MechHomePageResource, AboutiitgmechResource, EventHomePageResource, EventPageResource, CategoriesHomeResource, CategoriesResource, FacultyHomePageResource, FacultyPageResource, StudentHomePageResource, StudentPageResource, StaffHomePageResource, StaffPageResource, AlumniHomePageResource, AlumnusPageResource, ResearchHomePageResource, ResearchLabHomePageResource, ResearchLabPageResource, PublicationHomePageResource, PublicationPageResource, ProjectHomePageResource, ProjectPageResource, CourseStructureResource, CoursePageResource, AwardHomePageResource)

with open('mechweb/automation_scripts/tsvs/CustomUser.tsv', mode='w') as tsv_file:
	CustomUser = CustomUserResource().export()
	print(CustomUser.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/MechHomePage.tsv', mode='w') as tsv_file:
	MechHomePage = MechHomePageResource().export()
	print(MechHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/Aboutiitgmech.tsv', mode='w') as tsv_file:
	Aboutiitgmech = AboutiitgmechResource().export()
	print(Aboutiitgmech.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/EventHomePage.tsv', mode='w') as tsv_file:
	EventHomePage = EventHomePageResource().export()
	print(EventHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/EventPage.tsv', mode='w') as tsv_file:
	EventPage = EventPageResource().export()
	print(EventPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/CategoriesHome.tsv', mode='w') as tsv_file:
	CategoriesHome = CategoriesHomeResource().export()
	print(CategoriesHome.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/Categories.tsv', mode='w') as tsv_file:
	Categories = CategoriesResource().export()
	print(Categories.tsv, file=tsv_file), file=tsv_file

with open('mechweb/automation_scripts/tsvs/FacultyHomePage.tsv', mode='w') as tsv_file:
	FacultyHomePage = FacultyHomePageResource().export()
	print(FacultyHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/FacultyPage.tsv', mode='w') as tsv_file:
	FacultyPage = FacultyPageResource().export()
	print(FacultyPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/StudentHomePage.tsv', mode='w') as tsv_file:
	StudentHomePage = StudentHomePageResource().export()
	print(StudentHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/StudentPage.tsv', mode='w') as tsv_file:
	StudentPage = StudentPageResource().export()
	print(StudentPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/StaffHomePage.tsv', mode='w') as tsv_file:
	StaffHomePage = StaffHomePageResource().export()
	print(StaffHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/StaffPage.tsv', mode='w') as tsv_file:
	StaffPage = StaffPageResource().export()
	print(StaffPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/AlumniHomePage.tsv', mode='w') as tsv_file:
	AlumniHomePage = AlumniHomePageResource().export()
	print(AlumniHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/AlumnusPage.tsv', mode='w') as tsv_file:
	AlumnusPage = AlumnusPageResource().export()
	print(AlumnusPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/ResearchHomePage.tsv', mode='w') as tsv_file:
	ResearchHomePage = ResearchHomePageResource().export()
	print(ResearchHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/ResearchLabHomePage.tsv', mode='w') as tsv_file:
	ResearchLabHomePage = ResearchLabHomePageResource().export()
	print(ResearchLabHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/ResearchLabPage.tsv', mode='w') as tsv_file:
	ResearchLabPage = ResearchLabPageResource().export()
	print(ResearchLabPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/PublicationHomePage.tsv', mode='w') as tsv_file:
	PublicationHomePage = PublicationHomePageResource().export()
	print(PublicationHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/PublicationPage.tsv', mode='w') as tsv_file:
	PublicationPage = PublicationPageResource().export()
	print(PublicationPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/ProjectHomePage.tsv', mode='w') as tsv_file:
	ProjectHomePage = ProjectHomePageResource().export()
	print(ProjectHomePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/ProjectPage.tsv', mode='w') as tsv_file:
	ProjectPage = ProjectPageResource().export()
	print(ProjectPage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/CourseStructure.tsv', mode='w') as tsv_file:
	CourseStructure = CourseStructureResource().export()
	print(CourseStructure.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/CoursePage.tsv', mode='w') as tsv_file:
	CoursePage = CoursePageResource().export()
	print(CoursePage.tsv, file=tsv_file)

with open('mechweb/automation_scripts/tsvs/AwardHomePage.tsv', mode='w') as tsv_file:
	AwardHomePage = AwardHomePageResource().export()
	print(AwardHomePage.tsv, file=tsv_file)