from django.contrib import admin
from .models import Feedback, FeedbackAdmin, Telebot, TelebotAdmin

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Telebot, TelebotAdmin)