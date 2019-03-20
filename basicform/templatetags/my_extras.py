from django import templates

register = templates.Library()

@register.filter('cut')
def cut(val, arg):
    return val.replace(arg, '')

# register.filter('cut', cut)