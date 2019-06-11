Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 20, in <module>
    user_type = USER_TYPES[row["user_type"]][0],
TypeError: tuple indices must be integers or slices, not str
>>> from mechweb.automation_scripts import import_users
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 25, in <module>
    password = row["password"],
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 422, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/contrib/auth/base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 741, in save
    force_update=force_update, update_fields=update_fields)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 790, in save_base
    update_fields=update_fields, raw=raw, using=using,
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in send
    for receiver in self._live_receivers(sender)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in <listcomp>
    for receiver in self._live_receivers(sender)
  File "/home/webops/iitg_mechanical_website/mechweb/wagtail_hooks.py", line 62, in create_user_profile
    home.add_child(instance=new_student)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 1013, in add_child
    return MP_AddChildHandler(self, **kwargs).process()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 389, in process
    newobj.save()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 442, in save
    self.full_clean()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 432, in full_clean
    super().full_clean(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'slug': ['This slug is already in use'], 'user': ['Student with this User already exists.'], 'email_id': ['Student with this Email id already exists.'], 'roll_no': ['Student with this Roll no already exists.']}
>>> 
>>> from mechweb.automation_scripts import import_users
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 25, in <module>
    password = row["password"],
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 422, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/contrib/auth/base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 741, in save
    force_update=force_update, update_fields=update_fields)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 790, in save_base
    update_fields=update_fields, raw=raw, using=using,
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in send
    for receiver in self._live_receivers(sender)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in <listcomp>
    for receiver in self._live_receivers(sender)
  File "/home/webops/iitg_mechanical_website/mechweb/codewa.py", line 61, in create_user_profile
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 1013, in add_child
    return MP_AddChildHandler(self, **kwargs).process()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 389, in process
    newobj.save()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 442, in save
    self.full_clean()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 432, in full_clean
    super().full_clean(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'slug': ['This slug is already in use'], 'email_id': ['Student with this Email id already exists.'], 'roll_no': ['Student with this Roll no already exists.']}
>>> from mechweb.automation_scripts import import_users
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 25, in <module>
    password = row["password"],
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 422, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/contrib/auth/base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 741, in save
    force_update=force_update, update_fields=update_fields)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 790, in save_base
    update_fields=update_fields, raw=raw, using=using,
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in send
    for receiver in self._live_receivers(sender)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in <listcomp>
    for receiver in self._live_receivers(sender)
  File "/home/webops/iitg_mechanical_website/mechweb/codewa.py", line 61, in create_user_profile
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 1013, in add_child
    return MP_AddChildHandler(self, **kwargs).process()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 389, in process
    newobj.save()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 442, in save
    self.full_clean()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 432, in full_clean
    super().full_clean(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'slug': ['This slug is already in use'], 'email_id': ['Student with this Email id already exists.'], 'roll_no': ['Student with this Roll no already exists.']}
>>> from mechweb.automation_scripts import import_users
Traceback (most recent call last):
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 383, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: UNIQUE constraint failed: mechweb_customuser.username

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 25, in <module>
    password = row["password"],
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 422, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/contrib/auth/base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 741, in save
    force_update=force_update, update_fields=update_fields)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 779, in save_base
    force_update, using, update_fields,
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 870, in _save_table
    result = self._do_insert(cls._base_manager, using, fields, update_pk, raw)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 908, in _do_insert
    using=using, raw=raw)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 1186, in _insert
    return query.get_compiler(using=using).execute_sql(return_id)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 1335, in execute_sql
    cursor.execute(sql, params)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 99, in execute
    return super().execute(sql, params)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 67, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 76, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/utils.py", line 89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 383, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: UNIQUE constraint failed: mechweb_customuser.username
>>> 
>>> from mechweb.automation_scripts import import_users
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/webops/iitg_mechanical_website/mechweb/automation_scripts/import_users.py", line 25, in <module>
    password = row["password"],
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/query.py", line 422, in create
    obj.save(force_insert=True, using=self.db)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/contrib/auth/base_user.py", line 66, in save
    super().save(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 741, in save
    force_update=force_update, update_fields=update_fields)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 790, in save_base
    update_fields=update_fields, raw=raw, using=using,
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in send
    for receiver in self._live_receivers(sender)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/dispatch/dispatcher.py", line 175, in <listcomp>
    for receiver in self._live_receivers(sender)
  File "/home/webops/iitg_mechanical_website/mechweb/wagtail_hooks.py", line 62, in create_user_profile
    home.add_child(instance=new_student)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 1013, in add_child
    return MP_AddChildHandler(self, **kwargs).process()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/treebeard/mp_tree.py", line 389, in process
    newobj.save()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/contextlib.py", line 74, in inner
    return func(*args, **kwds)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 442, in save
    self.full_clean()
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/wagtail/core/models.py", line 432, in full_clean
    super().full_clean(*args, **kwargs)
  File "/home/webops/anaconda3/envs/mech/lib/python3.7/site-packages/django/db/models/base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'slug': ['This slug is already in use'], 'user': ['Student with this User already exists.'], 'email_id': ['Student with this Email id already exists.'], 'roll_no': ['Student with this Roll no already exists.']}
