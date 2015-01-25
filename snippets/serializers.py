from rest_framework_mongoengine.serializers import DocumentSerializer
from mongoengine import *
from snippets.models import Snippet

class SnippetSerializer(DocumentSerializer):
    class Meta:
        model = Snippet