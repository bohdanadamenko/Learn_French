from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given separator."""
    return value.split(arg)

@register.filter
def get_emoji(value):
    """Get the first word (emoji) from the title."""
    parts = value.split(' ', 1)
    return parts[0] if parts else ''

@register.filter
def get_text_after_emoji(value):
    """Get the text after the first word (emoji)."""
    parts = value.split(' ', 1)
    return parts[1] if len(parts) > 1 else ''
