from mechweb.models import FacultyResearchInterestTag

filewa = open('output.txt', 'w')
# def findCommonTags():
live_tags = FacultyResearchInterestTag.objects.all()
common_tags = []
for tag in live_tags:
	tag2 = tag.__str__().split('tagged with ', 1)
	print("Tag2: ", tag2, file=filewa)
	# print("+++++++++", file=filewa)
	tag3 = tag2.pop()
	print("Tag3: ", tag3, file=filewa)
	# print("0000000000", file=filewa)
	if tag3 not in common_tags:
		common_tags.append(tag3)
		print("common_tags: ", common_tags, file=filewa)
		# print("********", file=filewa)

# return common_tags
for tag in common_tags:
	print(tag, file=filewa)
	print("________", file=filewa)

filewa.close()


