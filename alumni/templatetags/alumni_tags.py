from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@stringfilter
@register.filter("noscrape")
def noscrape(value):
    if not value:
        return None
    return value.replace("@", "@<span hidden></span>")
