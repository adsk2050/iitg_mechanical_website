import datetime
from django import template
from django.template.defaultfilters import stringfilter
from wagtail.core.models import Page
import random, string

register = template.Library()


@stringfilter
@register.filter("noscrape")
def noscrape(value):
    if not value:
        return None
    return value.replace("@", "@<span hidden></span>")


@stringfilter
@register.filter("isalumni")
def isalumni(value):
    if (value) and (int(value) <= datetime.datetime.now().year):
        return f" ({value} batch alumnus) "
    else:
        return ""


@register.inclusion_tag("templatetags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 1:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }


@register.filter("randomid")
def randomString(size):
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=size))
