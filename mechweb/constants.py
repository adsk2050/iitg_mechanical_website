TEXT_PANEL_CONTENT_TYPES=(
	('0', 'News'),
	('1', 'Announcements'),
	('2', 'Others'),
)

USER_TYPES = (
	('0', 'Faculty'),
	('1', 'Student'),
	('2', 'Alumnus'),
	('3', 'Staff'),
)

LOCATIONS=(
	('0', 'Seminar hall'),
)

EVENTS=(
	('0', 'Meeting'),
	('1', 'Seminar'),
	('2', 'Workshop'),
	('3', 'Informal event'),
	('4', 'Conference'),
	('5', 'PhD viva'),
)

STUDENT_PROGRAMME = (
	('0', 'Bachelor'),
	('1', 'Masters'),
	('2', 'Research Scholar'),
	('3', 'Other, e.g. PostDoc or N.A.'),
)

MASTERS_SPECIALIZATION = (
	('0', 'Not Applicable'),
	('1', 'Aerodynamics & Propulsion'),
	('2', 'Computer Aided Manufacturing'),
	('3', 'Computational Mechanics'),
	('4', 'Fluids and Thermal'),
	('5', 'Machine Design'),
)

STAFF_DESIGNATION = (
	('0', 'Administrative Staff'),
	# ('1', 'Project Staff'),
	('1', 'Lab Staff'),
	('2', 'Technicial staff'),
	('3', 'Others'),
)

PROJECT_TYPES=(
	('1','Academic'),
	('0','Consultancy')
)

PUBLICATION_TYPES = (
	('0', 'Poster'),
	('1', 'Conference Publication'),
	('2', 'Journal Publication'),
	('3', 'Patent'),
	('4', 'Books'),
	('5', 'Book Chapters'),
)

LAB_TYPES = (
	('0', 'UG Lab'),
	('1', 'PG Lab'),
)

LAB_RESEARCH_AREAS = (
	('0', 'Other'),
	('1', 'Machine Design Engineering'),
	('2', 'Manufacturing Engineering'),
	('3', 'Thermal and Fluid Engineering'),
)

COURSE_TYPES = (
	('Departmental', (
			('0', 'Core course'),
			('1', 'Department Elective'),
			('2', 'Department Open Elective'),
		),
	),
	('Non-Departmental', (
			('3', 'Common course'),
			('4', 'HSS Elective'),
			('4', 'Open Elective'),
		),
	),
)

# # EventHomePage NAV_ORDER[0] 5
# # FacultyHomePage NAV_ORDER[1] 2
# # StudentHomePage NAV_ORDER[2] 3
# # AlumniHomePage NAV_ORDER[3] 6
# # StaffHomePageNAV_ORDER[4] 7
# # ResearchHomePage NAV_ORDER[5] 1
# # CourseStructure NAV_ORDER[6] 4

# NAV_ORDER = [5, 2, 3, 6, 7, 1, 4]
# # # NAV_ORDER = (
# # # 	('0', 'Poster'),
# # # 	('1', 'Conference Publication'),
# # # 	('2', 'Journal Publication'),
# # # 	('3', 'Patent'),
# # # 	('4', 'Books'),
# # # 	('5', 'Book Chapters'),
# # # )
############################# Faculty
FACULTY_ROLES=(
	('2', 'Not Applicable'),
	('1', 'HoD'),
	('0', 'Director')
)

FACULTY_DESIGNATION = (
	('0', 'HAG'),
	('1', 'Professor'),
	('2', 'Assistant Professor'),
	('3', 'Associate Professor'),
	('4', 'Visiting Professor'),
	('5', 'Professor On lien'),
)

FACULTY_AWARD_TYPES = (
	('0', 'Faculty Awarded'),
	('1', 'Best Paper'),
	('2', 'Other'),
)

DPPC = (
	('6', 'Not Applicable'),
	('0', 'Chairman'),
	('1', 'Secretary'),
	('2', 'Faculty Member'),
	('3', 'External Member'),
	('4', 'PhD Student Member'),
	('5', 'MTech Student Member'),
)

DUPC = (
	('6', 'Not Applicable'),
	('0', 'Chairman'),
	('1', 'Secretary'),
	('2', 'Faculty Member'),
	('3', 'External Member'),
	('4', '3rd year BTech'),
	('5', '2nd year BTech'),
)

DISCIPLINARY_COMMITTEE = (
	('4', 'Not Applicable'),
	('0', 'Chairman'),
	('1', 'Secretary'),
	('2', 'Member Secretary'),
	('3', 'Student Member'),
)

FACULTY_IN_CHARGE = (
	('11', 'Not Applicable'),
	('0', 'BTP Co ordinator'),
	('1', 'MTP Co ordinator'),
	('2', 'Central Workshop'),
	('3', 'Library Committee'),
	('4', 'Training and Placement'),
	('5', 'Departmental Seminar Room'),
	('6', 'Secretary Faculty Meeting'),
	('7', 'PG Computational Lab'),
	('8', 'Research Scholar Room'),
	('9', 'Time Table Committee'),
	('10', 'Departmental Website'),
)

LABORATORY_IN_CHARGE = (
	('14', 'Not Applicable'),
	('0', 'Advanced Manufacturing Laboratory'),
	('1', 'CAD Laboratory'),
	('2', 'Central Workshop'),
	('3', 'Fluid Mechanics Laboratory'),
	('4', 'IC Engines Laboratory'),
	('5', 'Instrumentation and Control Laboratory'),
	('6', 'Material Science Laboratory'),
	('7', 'Tribology Laboratory'),
	('8', 'Mechatronics and Robotics Laboratory'),
	('9', 'Strength of Materials Laboratory'),
	('10', 'Theory of Machines Laboratory'),
	('11', 'Thermal Science Laboratory'),
	('12', 'Turbo Machinary Laboratory'),
	('13', 'Vibrations and Acoustics Laboratory'),
)

DISPOSAL_COMMITTEE = (
	('4', 'Not Applicable'),
	('0', 'Chairman'),
	('1', 'Member'),
	('2', 'External Member'),
	('3', 'Non Member Secretary'),
)

RESEARCH_AREAS = (
	('a', 'Thermal and Fluid Engineering'),
	('b', 'Machine Design Engineering'),
	('c', 'Manufacturing Engineering'),
)
