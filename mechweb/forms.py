from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from .constants import USER_TYPES
# from mechweb.models import CustomUserInline

# if you used this then comment admin edit panels
# -------------------------------------------------
class CustomUserEditForm(UserEditForm):
	middle_name = forms.CharField(label=_("Middle Name"), required=False)
	user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
	uid = forms.CharField(required=True, label=_("Roll No. / Employee ID"))
	is_staff = forms.BooleanField(label=_("Allow to access admin panel"))
	username = forms.CharField(label=_("User Name"), required=True)

	# def save(self, commit=True):
	# 	user = super(UserEditForm, self).save(commit=False)
	# 	# users can access django-admin iff they are a superuser
	# 	user.is_staff = self.is_staff
	# 	if self.cleaned_data["password1"]:
	# 		user.set_password(self.cleaned_data["password1"])
	# 	if commit:
	# 		user.save()
	# 		self.save_m2m()
	# 	return user   

    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


class CustomUserCreationForm(UserCreationForm):
	middle_name = forms.CharField(label=_("Middle Name"), required=False)
	user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
	uid = forms.CharField(required=True, label=_("Roll No. / Employee ID"))
	is_staff = forms.BooleanField(label=_("Allow to access admin panel"))
	username = forms.CharField(label=_("User Name"), required=True)
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))
# -------------------------------------------------


# standard_fields = set(['email', 'first_name', 'last_name', 'is_superuser', 'groups'])
# # UserCreationForm
# fields = set([User.USERNAME_FIELD]) | standard_fields | custom_fields
# # UserEditForm
# fields = set([User.USERNAME_FIELD, "is_active"]) | standard_fields | custom_fields