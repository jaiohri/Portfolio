# Images Directory

Place your logo and other images here.

## Recommended file formats:
- **Logo**: PNG with transparent background (preferred) or SVG
- **Other images**: PNG, JPG, or WebP

## Usage in templates:

To use images in your Django templates, use the static template tag:

```django
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

## Logo file suggestions:
- `logo.png` - Main logo
- `logo.svg` - Vector logo (scalable)
- `favicon.ico` - Browser favicon

