from django.db import models
from PIL import Image
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import requests
from django.core.exceptions import ValidationError
from datetime import date

class Client(models.Model):
    lastname = models.CharField(max_length=16, blank=False, null=False)
    firstname = models.CharField(max_length=16, blank=False, null=False)
    patronymic = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=36, blank=True, null=True, unique=True)
    num_contract = models.CharField(max_length=8, blank=False, null=False, unique=True)
    num_membership = models.CharField(max_length=8, blank=False, null=False, unique=True)
    date_start_contract = models.DateField(blank=False, null=False)
    date_end_contract = models.DateField(blank=True, null=False)
    type_membership = models.CharField(max_length=16, blank=False, null=False, choices=((i, i) for i in ('Безлимитный','Безлимитный')))
    time_period = models.IntegerField(blank=False, null=False, unique=False, default=1, choices=((i, i) for i in [1,3,6,12]))
    status_membership = models.CharField(max_length=16, blank=False, null=False, choices=((i, i) for i in ('Активный', 'Не активный')))
    birthdate = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=8, blank=False, null=False, choices=((i, i) for i in ('Мужчина', 'Женщина')))
    passport = models.TextField(max_length=350, blank=False, null=False)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'phone', 'num_contract', 'num_membership', 'date_end_contract', 'status_membership')
    list_display_links = ('lastname', 'phone', 'num_contract', 'num_membership')
    search_fields = ('lastname', 'firstname', 'phone', 'num_contract', 'num_membership')
    ordering = ['lastname', 'firstname', 'phone', 'num_contract', 'num_membership', 'date_end_contract', 'status_membership']
    list_filter = ('status_membership','type_membership')


class ArchiveJournalVisit(models.Model):
    num_membership = models.CharField(max_length=8, blank=False, null=False, unique=False)
    gender = models.CharField(max_length=8, blank=True, null=True, choices=((i, i) for i in ('Мужчина', 'Женщина')))
    date_start_visit = models.DateTimeField(blank=False, null=True)
    date_end_visit = models.DateTimeField(blank=False, null=True)
    locker_number = models.IntegerField(blank=False, null=False, unique=False, default=1, choices=((i, i) for i in range(1, 31)))

class ArchiveJournalVisitAdmin(admin.ModelAdmin):
    list_display = ('num_membership', 'date_start_visit', 'date_end_visit', 'gender', 'locker_number')
    list_display_links = ('num_membership',)
    search_fields = ('num_membership',)
    ordering = ['num_membership', 'date_start_visit', 'date_end_visit', 'gender', 'locker_number']
    list_filter = ('gender',)


class journalVisit(models.Model):
    is_cleaned = False
    num_membership = models.CharField(max_length=8, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=8, blank=True, null=True, choices=((i, i) for i in ('Мужчина', 'Женщина')))
    date_start_visit = models.DateTimeField(blank=False, null=True)
    date_end_visit = models.DateTimeField(blank=True, null=True)
    locker_number = models.IntegerField(blank=False, null=False, unique=True, default=1, choices=((i, i) for i in range(1, 31)))

    def clean(self):
        self.is_cleaned = True
        num_membership = self.num_membership
        obj = Client.objects.filter(num_membership=num_membership).first()
        if obj:
            if obj.status_membership == 'Не активный':
                raise ValidationError(f"Абонимент {num_membership} не действителен!")
            elif obj.date_end_contract < date.today():
                obj.status_membership = 'Не активный'
                obj.save()
                raise ValidationError(f"Абонимент {num_membership} не действителен!")
        else:
            raise ValidationError(f"Абонимент {num_membership} не найден в базе!")

        super(journalVisit, self).clean()

    def save(self, *args, **kwargs):
        date_end_visit=self.date_end_visit
        num_membership=self.num_membership
        gender=self.gender
        date_start_visit=self.date_start_visit
        locker_number=self.locker_number
        obj = Client.objects.filter(num_membership=num_membership).first()
        if obj.status_membership == 'Активный':
            super(journalVisit, self).save(*args, **kwargs)
        if date_end_visit:
            ArchiveJournalVisit.objects.create(num_membership=num_membership, gender=gender,
                                                           date_start_visit=date_start_visit, date_end_visit=date_end_visit, locker_number=locker_number)
            obj_del = journalVisit.objects.filter(num_membership=num_membership).first()
            obj_del.delete()


class journalVisitAdmin(admin.ModelAdmin):
    list_display = ('num_membership', 'date_start_visit', 'gender', 'locker_number')
    list_display_links = ('num_membership',)
    search_fields = ('num_membership',)
    ordering = ['num_membership', 'date_start_visit', 'gender', 'locker_number']
    list_filter = ('gender',)

class Trener(models.Model):
    lastnameTrener = models.CharField(max_length=16, blank=False, null=False)
    firstnameTrener = models.CharField(max_length=16, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False, unique=True)
    type_trains = models.CharField(max_length=16, blank=False, null=False,
                                       choices=((i, i) for i in ('Персональные', 'Групповые')))
    adwards = models.TextField(max_length=250, blank=True, null=True)
    photo = models.ImageField(default='default.jpg', upload_to='train_pics')

    def __str__(self):
        return self.lastnameTrener+' '+self.firstnameTrener


class TrenerAdmin(admin.ModelAdmin):
    list_display = ('lastnameTrener', 'firstnameTrener', 'phone', 'type_trains')
    list_display_links = ('lastnameTrener',)
    search_fields = ('lastnameTrener', 'firstnameTrener')
    ordering = ['lastnameTrener', 'firstnameTrener', 'phone', 'type_trains']
    list_filter = ('type_trains',)

class Train(models.Model):
    trener = models.ManyToManyField(Trener)
    # trener = models.OneToOneField(Trener, on_delete=models.DO_NOTHING, primary_key = True, null=False)
    membership_or_fio = models.CharField(max_length=48, blank=False, null=False)
    type_trains = models.CharField(max_length=16, blank=False, null=False,
                                       choices=((i, i) for i in ('Персональная', 'Групповая')))
    dateTime = models.DateTimeField(blank=False, null=False)
    visited = models.BooleanField(default=False)


    def get_treners(self):
        return "\n".join([str(p) for p in self.trener.all()])

class TrainAdmin(admin.ModelAdmin):
    list_display = ('get_treners', 'membership_or_fio', 'type_trains', 'dateTime', 'visited')
    list_display_links = ('get_treners', 'dateTime')
    search_fields = ('get_treners', 'membership_or_fio', 'dateTime')
    ordering = ['membership_or_fio', 'type_trains', 'dateTime', 'visited']
    list_filter = ('trener','type_trains', 'visited')
