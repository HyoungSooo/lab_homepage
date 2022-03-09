from email.mime import image
from os import link
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

YEARTOCHOICES = {
    ("2023", 2023),
    ("2022", 2022),
    ("2021", 2021),
    ("2020", 2020),
    ("2019", 2019),
    ("2018", 2018),
    ("2017", 2017),
    ("2016", 2016),
    ("2015", 2015)
}

CATAGORY = {
    ('Professor', 'Professor'), ('Research Collaborators',
                                 'Research Collaborators'), ('Research Professor', 'Research Professor'),
    ('PhD Students', 'PhD Students'), ('MS Students',
                                       'MS Students'), ('Undergraduate', 'Undergraduate')
}


class WhatWeDo(models.Model):
    title = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=300)


class IntroduceUs(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=40, unique=True, blank=False)
    Affiliation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='indexpage')
    category = models.CharField(max_length=40, choices=CATAGORY, blank=False)

    def __str__(self):
        return self.name


class OtherLink(models.Model):
    introduceus = models.ForeignKey(
        IntroduceUs, on_delete=models.CASCADE, related_name="other_link")
    link_name = models.CharField(max_length=30, blank=False)
    link = models.URLField("Site URL")


class AlumniPhD(models.Model):
    name = models.CharField(max_length=30, blank=False)
    company = models.CharField(max_length=50)
    email = models.EmailField()


class AlumniMs(models.Model):
    name = models.CharField(max_length=30, blank=False)
    company = models.CharField(max_length=50)
    email = models.EmailField()


class PhotosTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PhotosTitle_Photos(models.Model):
    title = models.ForeignKey(
        PhotosTitle, on_delete=models.CASCADE, related_name='PhotoTitle')
    where = models.CharField(max_length=300, blank=True, default='')
    address = models.CharField(max_length=300, blank=True, default='')
    image = models.ImageField(upload_to='photos')


class PublicationsYears(models.Model):
    year = models.CharField(
        max_length=30, choices=YEARTOCHOICES, blank=False, unique=True)

    def __str__(self):
        return self.year


class Publications(models.Model):
    year = models.ForeignKey(
        PublicationsYears, on_delete=models.CASCADE, related_name='Publications')
    image = models.ImageField(upload_to='publications')
    title = models.CharField(max_length=300, unique=True, blank=False)
    link = models.URLField()
    where_to_find = models.CharField(max_length=100)

    def __str__(self):
      return self.title

class PublicationsMembers(models.Model):
    Publications = models.ForeignKey(
        Publications, on_delete=models.CASCADE, related_name='Members')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
