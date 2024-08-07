from django import template

register = template.Library()

@register.simple_tag
def add_path(data):
    if data:
        return f'/media/{data}'
    return '#'


@register.simple_tag
def get_value(dict, key):
    return dict.get(key)
