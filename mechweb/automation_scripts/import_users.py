import csv
from mechweb import wagtail_hooks
from mechweb.models import CustomUser
USER_TYPES = (
	('0', 'Faculty'),
	('1', 'Student'),
	('2', 'Alumnus'),
	('3', 'Staff'),
)

with open('mechweb/automation_scripts/users.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
        	pass
        	#can add to check csv format
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
        line_count += 1
