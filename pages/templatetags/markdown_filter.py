import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(text):
    """Convert markdown text to HTML"""
    if not text:
        return ''
    md = markdown.Markdown(extensions=['nl2br', 'fenced_code'])
    return mark_safe(md.convert(text))

