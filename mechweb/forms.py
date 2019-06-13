from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from .constants import USER_TYPES
# from mechweb.models import CustomUserInline

# if you used this then comment admin edit panels
# -------------------------------------------------
class CustomUserEditForm(UserEditForm):
    user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
    is_staff = forms.BooleanField(required=True, label=_("Editor Access"))
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
    is_staff = forms.BooleanField(required=True, label=_("Editor Access"))
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))
# -------------------------------------------------


# standard_fields = set(['email', 'first_name', 'last_name', 'is_superuser', 'groups'])
# # UserCreationForm
# fields = set([User.USERNAME_FIELD]) | standard_fields | custom_fields
# # UserEditForm
# fields = set([User.USERNAME_FIELD, "is_active"]) | standard_fields | custom_fields