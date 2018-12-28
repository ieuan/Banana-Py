from django import template
from django.utils.html import format_html

from banana_py import Bananas_OAuth

register = template.Library()

@register.simple_tag
def banana_auth_url(link_text):
    return format_html("<a href=\"{}\">{}</a>", Bananas_OAuth().authorize_url(), link_text)
