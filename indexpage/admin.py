from django.contrib import admin
from . import models

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.AlumniMs)
admin.site.register(models.AlumniPhD)
admin.site.register(models.IntroduceUs)
admin.site.register(models.OtherLink)
admin.site.register(models.PhotosTitle)
admin.site.register(models.PhotosTitle_Photos)
admin.site.register(models.Publications)
admin.site.register(models.PublicationsMembers)
admin.site.register(models.PublicationsYears)
admin.site.register(models.WhatWeDo)
