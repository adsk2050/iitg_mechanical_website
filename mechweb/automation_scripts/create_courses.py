import csv
from mechweb import wagtail_hooks
from mechweb.models import CoursePage, CourseStructure

from django.utils.text import slugify

STUDENT_PROGRAMME = (
	('0', 'Bachelor'),
	('1', 'Masters'),
	('2', 'Research Scholar'),
	('3', 'Other'),
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
			('5', 'Open Elective'),
		),
	),
)

# if CourseStructure.objects.all():
course_structure = CourseStructure.objects.all()[0]
with open('mechweb/automation_scripts/courses.tsv', mode='r') as tsv_file:
	tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
	line_count = 0
	logf = open("mechweb/automation_scripts/course_errors.log", "a")
	logf.write("----------------------------------\nAdding courses on  {0}\n----------------------------------\n".format(datetime.datetime.now() ))
	for row in tsv_reader:
		if line_count == 0:
			pass
		#can add to check csv format
		# if row["course_page_link"] == "":
		# 	course_page_link = course_structure.url+"/"+row["code"]
		# else:
		# 	course_page_link = row["course_page_link"]
		try:
			course=CoursePage(
				title=row["name"],
				slug=CoursePage()._get_autogenerated_slug(slugify(row["code"])),
				name = row["name"],
				code = row["code"],
				lectures = row["lectures"],
				tutorials = row["tutorials"],
				practicals = row["practicals"],
				credits = row["credits"],
				semester = row["semester"],
				course_type = row["course_type"],
				eligible_programmes = row["eligible_programmes"],
				course_page_link = row["course_page_link"],
				description = row["description"],
			)
			course_structure.add_child(instance=course)
			course_structure.save()
		except Exception as e:
			logf.write("Failed to add {0} due to  {1}\n".format(str(row["code"]), str(e)))
		line_count += 1
	logf.close()



# img_dnbasu = open('/media/original_images/dnbasu.jpg', mode='r')