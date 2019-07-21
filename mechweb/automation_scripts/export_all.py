
from mechweb.admin import(CustomUserResource, MechHomePageResource, AboutiitgmechResource, EventHomePageResource, EventPageResource, CategoriesHomeResource, CategoriesResource, FacultyHomePageResource, FacultyPageResource, StudentHomePageResource, StudentPageResource, StaffHomePageResource, StaffPageResource, AlumniHomePageResource, AlumnusPageResource, ResearchHomePageResource, ResearchLabHomePageResource, ResearchLabPageResource, PublicationHomePageResource, PublicationPageResource, ProjectHomePageResource, ProjectPageResource, CourseStructureResource, CoursePageResource, AwardHomePageResource)

with open('mechweb/automation_scripts/tsvs/CustomUser.tsv', mode='w') as tsv_file:
	CustomUser = CustomUserResource().export()
	tsv_file.write("{0}".format(CustomUser.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/MechHomePage.tsv', mode='w') as tsv_file:
	MechHomePage = MechHomePageResource().export()
	tsv_file.write("{0}".format(MechHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/Aboutiitgmech.tsv', mode='w') as tsv_file:
	Aboutiitgmech = AboutiitgmechResource().export()
	tsv_file.write("{0}".format(Aboutiitgmech.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/EventHomePage.tsv', mode='w') as tsv_file:
	EventHomePage = EventHomePageResource().export()
	tsv_file.write("{0}".format(EventHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/EventPage.tsv', mode='w') as tsv_file:
	EventPage = EventPageResource().export()
	tsv_file.write("{0}".format(EventPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/CategoriesHome.tsv', mode='w') as tsv_file:
	CategoriesHome = CategoriesHomeResource().export()
	tsv_file.write("{0}".format(CategoriesHome.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/Categories.tsv', mode='w') as tsv_file:
	Categories = CategoriesResource().export()
	tsv_file.write("{0}".format(Categories.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/FacultyHomePage.tsv', mode='w') as tsv_file:
	FacultyHomePage = FacultyHomePageResource().export()
	tsv_file.write("{0}".format(FacultyHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/FacultyPage.tsv', mode='w') as tsv_file:
	FacultyPage = FacultyPageResource().export()
	tsv_file.write("{0}".format(FacultyPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/StudentHomePage.tsv', mode='w') as tsv_file:
	StudentHomePage = StudentHomePageResource().export()
	tsv_file.write("{0}".format(StudentHomePage.tsv))
tsv_file.close()

with open('mechweb/automation_scripts/tsvs/StudentPage.tsv', mode='w') as tsv_file:
	StudentPage = StudentPageResource().export()
	tsv_file.write("{0}".format(StudentPage.tsv))
tsv_file.close()

with open('mechweb/automation_scripts/tsvs/StaffHomePage.tsv', mode='w') as tsv_file:
	StaffHomePage = StaffHomePageResource().export()
	tsv_file.write("{0}".format(StaffHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/StaffPage.tsv', mode='w') as tsv_file:
	StaffPage = StaffPageResource().export()
	tsv_file.write("{0}".format(StaffPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/AlumniHomePage.tsv', mode='w') as tsv_file:
	AlumniHomePage = AlumniHomePageResource().export()
	tsv_file.write("{0}".format(AlumniHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/AlumnusPage.tsv', mode='w') as tsv_file:
	AlumnusPage = AlumnusPageResource().export()
	tsv_file.write("{0}".format(AlumnusPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/ResearchHomePage.tsv', mode='w') as tsv_file:
	ResearchHomePage = ResearchHomePageResource().export()
	tsv_file.write("{0}".format(ResearchHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/ResearchLabHomePage.tsv', mode='w') as tsv_file:
	ResearchLabHomePage = ResearchLabHomePageResource().export()
	tsv_file.write("{0}".format(ResearchLabHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/ResearchLabPage.tsv', mode='w') as tsv_file:
	ResearchLabPage = ResearchLabPageResource().export()
	tsv_file.write("{0}".format(ResearchLabPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/PublicationHomePage.tsv', mode='w') as tsv_file:
	PublicationHomePage = PublicationHomePageResource().export()
	tsv_file.write("{0}".format(PublicationHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/PublicationPage.tsv', mode='w') as tsv_file:
	PublicationPage = PublicationPageResource().export()
	tsv_file.write("{0}".format(PublicationPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/ProjectHomePage.tsv', mode='w') as tsv_file:
	ProjectHomePage = ProjectHomePageResource().export()
	tsv_file.write("{0}".format(ProjectHomePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/ProjectPage.tsv', mode='w') as tsv_file:
	ProjectPage = ProjectPageResource().export()
	tsv_file.write("{0}".format(ProjectPage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/CourseStructure.tsv', mode='w') as tsv_file:
	CourseStructure = CourseStructureResource().export()
	tsv_file.write("{0}".format(CourseStructure.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/CoursePage.tsv', mode='w') as tsv_file:
	CoursePage = CoursePageResource().export()
	tsv_file.write("{0}".format(CoursePage.tsv))
	tsv_file.close()

with open('mechweb/automation_scripts/tsvs/AwardHomePage.tsv', mode='w') as tsv_file:
	AwardHomePage = AwardHomePageResource().export()
	tsv_file.write("{0}".format(AwardHomePage.tsv))
	tsv_file.close()
