from taggit.utils import parse_tags
from taggit.models import Tag
from mechweb.models import StudentPage, StudentResearchInterestTag

students = StudentPage.objects.all()
for student in students:
	""" put string of comma separated tags """
	tagstring =''
	words = parse_tags(tagstring)
	tag_list = []
	for word in words:
		tag = Tag(name=word)
		tag.save()
		taggedItem = StudentResearchInterestTag(
			tag=tag,
			content_object=student,
		)
		taggedItem.save()

tagstring ='C, C++, Algorithms, Data structures'
wkords = parse_tags(tagstring)
# tag_list = []
for word in words:
	abhay.research_interests.set(word)
abhay.save()
