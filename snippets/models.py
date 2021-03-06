from django.db import models
from mongoengine import *

connect('mydb')
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(Document):
    created = DateTimeField()
    title = StringField(max_length=100, default='')
    code = StringField()
    linenos = BooleanField(default=False)
    language = StringField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = StringField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)