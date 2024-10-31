from .models import *
from rest_framework import viewsets
from xy_django_serializer.Serializer import *


# Serializers define the API representation.
class xy_django_app_feedback_FeedbackSerializer(Serializer):

    default_value = ""

    class Meta:
        model = Feedback
        fields = "__all__"


# ViewSets define the view behavior.
class xy_django_app_feedback_FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = xy_django_app_feedback_FeedbackSerializer
