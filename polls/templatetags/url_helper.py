from django import template

register = template.Library()
@register.simple_tag
def GET_BASE_URL():
    return 'http://127.0.0.1:8000/'

