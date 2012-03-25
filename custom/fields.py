# HexColorField
import re
from django.db.models.fields import CharField
from django.forms import ValidationError, fields
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ImproperlyConfigured

# ResizedImageField
from PIL import Image

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from django.db.models.fields.files import ImageField, ImageFieldFile
from django.core.files.base import ContentFile


class ResizedImageFieldFile(ImageFieldFile):

    def _update_ext(filename, new_ext):
        parts = filename.split('.')
        parts[-1] = new_ext
        return '.'.join(parts)

    def save(self, name, content, save=True):
        new_content = StringIO()
        content.file.seek(0)

        img = Image.open(content.file)
        img.thumbnail((
            self.field.max_width,
            self.field.max_height
            ), Image.ANTIALIAS)
        img.save(new_content, format=self.field.format)

        new_content = ContentFile(new_content.getvalue())
        new_name = self._update_ext(name, self.field.format.lower())

        super(ResizedImageFieldFile, self).save(new_name, new_content, save)


class ResizedImageField(ImageField):

    attr_class = ResizedImageFieldFile

    def __init__(self, max_width=100, max_height=100, format='PNG', *args,
                 **kwargs):
        self.max_width = max_width
        self.max_height = max_height
        self.format = format
        super(ResizedImageField, self).__init__(*args, **kwargs)

