from django.contrib import admin
from .models import *


@admin.register(MFeedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("username", "text")
    filter_horizontal = ["images"]
