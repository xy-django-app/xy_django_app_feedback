from django.contrib import admin
from .models import *
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'text')
    filter_horizontal = ["images"]

admin.site.register(Feedback, FeedbackAdmin)
