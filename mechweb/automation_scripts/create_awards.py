import csv
import datetime
from mechweb import wagtail_hooks
from mechweb.models import CustomUser, AwardHomePage, Award


fac_award_types = (
    ('0', 'Faculty Awarded'),
    ('1', 'Best Paper'),
    ('2', 'Other'),
)

award_home = AwardHomePage.objects.all()[0]
award_number = Award.objects.all().count()
with open('mechweb/automation_scripts/awards.tsv', mode='r') as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
    line_count = 0
    logf = open("mechweb/automation_scripts/awd_errors.log", "a")
    logf.write("----------------------------------\nAdding awards on  {0}\n----------------------------------\n".format(datetime.datetime.now() ))
    for row in tsv_reader:
        if line_count == 0:
        	pass
        	#can add to check csv format
        try:
            print("Creating award: {}".format(str(row["award_title"])))
  
            awd=Award(
                page = award_home,
                alt_recipient_text = row["alt_recipient_text"],
                award_title = row["award_title"],
                award_description = row["award_description"],
                award_type = row["award_type"],
                award_time = row["award_time"],
                conferrer = row["conferrer"],
                conferrer_description = row["conferrer_description"],
                link = row["link"],
            )
            # award_home.add_child(instance=pub)
            awd.save()
            award_home.save()
            print("Created!")
        except Exception as e:
            #logf.write("{0}\n".format(str(e)))
            logf.write("Failed to add award. no. {0} | {1} due to {2}\n".format(line_count], str(row["name"]), str(e)))
        line_count += 1
    logf.close()

# # for deleting the award
# from mechweb.models import Award
# for awd in Award.objects.all():
#     print("Deleting",awd.award_title)
#     awd.delete()
#     print("Deleted!")

