import datetime
import csv
from mechweb import wagtail_hooks
from mechweb.models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.utils.text import slugify

user_type_choices = {
    '0':'Faculty',
    '1':'Student',
    '2':'Alumni',
    '3':'Staff',
    '4':'Others',
}

#### One problem is that even if I am running same code for adding user's groups in the first for loop, its not happening... but if I add the code after... the passwords are set and groups are set... why?

with open('mechweb/automation_scripts/users.tsv', mode='r') as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
    line_count = 0
    logf = open("mechweb/automation_scripts/user_errors.log", "a")
    logf.write("----------------------------------\nAdding users on  {0}\n----------------------------------\n".format(datetime.datetime.now() ))
    for row in tsv_reader:
        if line_count == 0:
        	pass
        	#can add to check csv format
        try:
            print("Creating {0} ...".format(str(row["first_name"]+" "+row["middle_name"]+" "+row["last_name"])))
            user=CustomUser.objects.create(
            	is_staff = True,
            	user_type = row["user_type"], 
    			username = slugify(row["username"]), 
                first_name = row["first_name"], 
    			middle_name = row["middle_name"], 
    			last_name = row["last_name"], 
    			email = row["email"], 
    			password = row["password"],
                uid=row["uid"],
            )
            user.set_password(user.password)
            user.save()
            group_name_int=user.user_type
            group_name_str=str(group_name_int)
            group_name=user_type_choices[group_name_str]
            user_group = Group.objects.get_or_create(name=group_name)
            x, y = user_group
            user.groups.add(x.id)
            user.save()
            print("Created!")
        except Exception as e:
            logf.write("Failed to add {0} due to  {1}\n".format(str(row["username"]), str(e)))
        line_count += 1
    logf.close()

# for user in CustomUser.objects.all().exclude(username='mechadmin'):
#     user.set_password(user.password)
#     user.save()

# for user in CustomUser.objects.all():
#     if user.email == 'mechadmin@iitg.ac.in':
#         pass
#     else:
#         group_name_int=user.user_type
#         group_name_str=str(group_name_int)
#         group_name=user_type_choices[group_name_str]
#         user_group = Group.objects.get_or_create(name=group_name)
#         x, y = user_group
#         user.groups.add(x.id)
#         user.save()

# for user in CustomUser.objects.all():
#     if user.email == 'mechadmin@iitg.ac.in':
#         pass
#     else:
#         user.set_password(user.password)
#         user.save()



########### For testing purposes
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

# user=CustomUser.objects.get(email='webweb@iitg.ac.in')
# user.delete()
# user=CustomUser.objects.create(
#     is_staff = True,
#     user_type = 4, 
#     username = 'webweb', 
#     first_name = 'Web', 
#     last_name = 'Web', 
#     email = 'webweb@iitg.ac.in', 
#     password = 'webwebmechweb@12345l789',
#     uid='000000000',
# )
# group_name_int=user.user_type
# group_name_str=str(group_name_int)
# group_name=user_type_choices[group_name_str]
# user_group = Group.objects.get_or_create(name=group_name)
# x, y = user_group
# user.groups.add(x.id)
# user.save()
# # user_group.user_set.add(user)
# # user.save()
# user.set_password(user.password)
# user.save()

# user_type_choices = {
#     '0':'Faculty',
#     '1':'Student',
#     '2':'Alumni',
#     '3':'Staff',
#     '4':'Others',
# }

# for user in CustomUser.objects.all():
#     if user.email == 'mechadmin@iitg.ac.in':
#         pass
#     else:
#         group_name_int=user.user_type
#         group_name_str=str(group_name_int)
#         group_name=user_type_choices[group_name_str]
#         user_group = Group.objects.get_or_create(name=group_name)
#         x, y = user_group
#         user.groups.add(x.id)
#         user.save()

# delete all users except admin
# import csv
# from mechweb import wagtail_hooks
# from mechweb.models import CustomUser
# from django.contrib.auth.models import Group, Permission
# from django.utils.text import slugify
# for c in CustomUser.objects.all().exclude(username='mechadmin'):
#     n = c.username
#     print("deleting: ", n)
#     c.delete()
#     print("deleted: ", n)