from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class Feedback(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'complete')
    list_display_links = ('name', 'phone')
    list_filter = ('complete',)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

class Telebot(models.Model):
    user_id_telegram = models.CharField(max_length=16)
    username_telegram = models.CharField(max_length=16)
    user_name_telegram = models.CharField(max_length=16)
    type_train = models.CharField(max_length=16)
    trener = models.CharField(max_length=26)
    user_name_client = models.CharField(max_length=16)
    user_phone_client = models.CharField(max_length=16)
    user_time_client = models.CharField(max_length=36)
    status = models.BooleanField(default=False)

class TelebotAdmin(admin.ModelAdmin):
    list_display = ('user_id_telegram', 'username_telegram', 'user_name_client', 'user_phone_client', 'user_time_client', 'status')
    list_display_links = ('user_id_telegram', 'username_telegram', 'user_name_client')
    search_fields = ('user_id_telegram', 'username_telegram', 'user_name_client','user_phone_client')
    list_filter = ('status',)