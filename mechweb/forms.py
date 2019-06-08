from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from .constants import USER_TYPES
# from mechweb.models import CustomUserInline

# if you used this then comment admin edit panels
# -------------------------------------------------
class CustomUserEditForm(UserEditForm):
    user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(required=True, choices=USER_TYPES, label=_("User Type"))
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))
# -------------------------------------------------
