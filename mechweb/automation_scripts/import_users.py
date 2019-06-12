import csv
from mechweb import wagtail_hooks
from mechweb.models import CustomUser
USER_TYPES = (
	('0', 'Faculty'),
	('1', 'Student'),
	('2', 'Alumnus'),
	('3', 'Staff'),
)

with open('mechweb/automation_scripts/users.tsv', mode='r') as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
    line_count = 0
    logf = open("mechweb/automation_scripts/user_errors.log", "a")
    for row in tsv_reader:
        if line_count == 0:
        	pass
        	#can add to check csv format
        try:
            user=CustomUser.objects.create(
            	is_staff = True,
            	user_type = row["user_type"], 
    			username = row["username"], 
    			first_name = row["first_name"], 
    			last_name = row["last_name"], 
    			email = row["email"], 
    			password = row["password"], 
            )
            user.save()
        except Exception as e:
            logf.write("Failed to add {0} due to  {1}\n".format(str(row["username"]), str(e)))
        line_count += 1
    logf.close()

# with open('mechweb/automation_scripts/users.tsv', mode='r') as tsv_file:
#     tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
#     line_count = 0
#     for row in tsv_reader:
#         if line_count == 0:
#             pass
#         user=CustomUser.objects.create(
#             is_staff = True,
#             user_type = row["user_type"], 
#             username = row["username"], 
#             first_name = row["first_name"], 
#             last_name = row["last_name"], 
#             email = row["email"], 
#             password = row["password"], 
#         )
#         user.save()
#         line_count += 1


