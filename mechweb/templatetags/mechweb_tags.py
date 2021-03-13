import datetime
from django import template
from django.template.defaultfilters import stringfilter
from wagtail.core.models import Page

register = template.Library()

@stringfilter
@register.filter('noscrape')
def noscrape(value):
    if '@' in value:
        return value.replace("@", " [at] ")
    else:
        return value

@stringfilter
@register.filter('noscrape')
def noscrape(value):
    if '@' in value:
        return value.replace("@", " [at] ")
    else:
        return value

@stringfilter
@register.filter('isalumni')
def noscrape(value):
    if int(value) <= datetime.datetime.now().year:
        return f" ({value} batch alumnus) "
    else:
        return ""

@register.inclusion_tag('templatetags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 1:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }