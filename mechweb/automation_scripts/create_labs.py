# import csv
# from mechweb import wagtail_hooks
# from mechweb.models import CustomUser
# from django.contrib.auth.models import Group, Permission

# user_type_choices = {
#     '0':'Faculty',
#     '1':'Student',
#     '2':'Alumni',
#     '3':'Staff',
#     '4':'Others',
# }


# with open('mechweb/automation_scripts/users.tsv', mode='r') as tsv_file:
#     tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
#     line_count = 0
#     logf = open("mechweb/automation_scripts/user_errors.log", "a")
#     for row in tsv_reader:
#         if line_count == 0:
#         	pass
#         	#can add to check csv format
#         try:
#             user=CustomUser.objects.create(
#             	is_staff = True,
#             	user_type = row["user_type"], 
#     			username = row["username"], 
#     			first_name = row["first_name"], 
#     			last_name = row["last_name"], 
#     			email = row["email"], 
#     			password = row["password"],
#                 uid=row["uid"],
#             )
#             group_name_int=user.user_type
#             group_name_str=str(group_name_int)
#             group_name=user_type_choices[group_name_str]
#             user_group = Group.objects.get_or_create(name=group_name)
#             x, y = user_group
#             user.groups.add(x.id)
#             user.save()
#             user.set_password(user.password)
#             user.save()
#         except Exception as e:
#             logf.write("Failed to add {0} due to  {1}\n".format(str(row["username"]), str(e)))
#         line_count += 1
#     logf.close()


# for user in CustomUser.objects.all():
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


# ########### For testing purposes
# # with open('mechweb/automation_scripts/users.tsv', mode='r') as tsv_file:
# #     tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab')
# #     line_count = 0
# #     for row in tsv_reader:
# #         if line_count == 0:
# #             pass
# #         user=CustomUser.objects.create(
# #             is_staff = True,
# #             user_type = row["user_type"], 
# #             username = row["username"], 
# #             first_name = row["first_name"], 
# #             last_name = row["last_name"], 
# #             email = row["email"], 
# #             password = row["password"], 
# #         )
# #         user.save()
# #         line_count += 1

# # user=CustomUser.objects.get(email='webweb@iitg.ac.in')
# # user.delete()
# # user=CustomUser.objects.create(
# #     is_staff = True,
# #     user_type = 4, 
# #     username = 'webweb', 
# #     first_name = 'Web', 
# #     last_name = 'Web', 
# #     email = 'webweb@iitg.ac.in', 
# #     password = 'webwebmechweb@12345l789',
# #     uid='000000000',
# # )
# # group_name_int=user.user_type
# # group_name_str=str(group_name_int)
# # group_name=user_type_choices[group_name_str]
# # user_group = Group.objects.get_or_create(name=group_name)
# # x, y = user_group
# # user.groups.add(x.id)
# # user.save()
# # # user_group.user_set.add(user)
# # # user.save()
# # user.set_password(user.password)
# # user.save()

# # user_type_choices = {
# #     '0':'Faculty',
# #     '1':'Student',
# #     '2':'Alumni',
# #     '3':'Staff',
# #     '4':'Others',
# # }

# # for user in CustomUser.objects.all():
# #     if user.email == 'mechadmin@iitg.ac.in':
# #         pass
# #     else:
# #         group_name_int=user.user_type
# #         group_name_str=str(group_name_int)
# #         group_name=user_type_choices[group_name_str]
# #         user_group = Group.objects.get_or_create(name=group_name)
# #         x, y = user_group
# #         user.groups.add(x.id)
# #         user.save()