from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MechwebConfig(AppConfig):
    name = 'mechweb'
    verbose_name = _('mechweb')

    # def ready(self):
    #     import mechweb.signals  # noqa