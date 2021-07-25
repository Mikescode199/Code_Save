from codeuser.models import Snippet
from rest_framework import routers, serializers, viewsets

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"