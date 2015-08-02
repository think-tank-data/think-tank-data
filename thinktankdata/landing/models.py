from django.db import models

# Create your models here.

class Sitewide(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    coverphoto = models.CharField(max_length=200)

class SubNotes(models.Model):
    subheadline = models.CharField(max_length=200)
    subtext = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(default=1)

class Categories(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(default=1)

class Tag(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(default=1)

class Thinktank(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    priority = models.PositiveSmallIntegerField(default=1)

class Person(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    priority = models.PositiveSmallIntegerField(default=1)

class Article(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    pub_date = models.DateTimeField('date published')
    headline = models.CharField(max_length=200)
    body = models.TextField()
    source = models.ForeignKey(Thinktank)
    author = models.ForeignKey(Person)

class Dataset(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(default=1)
    source = models.ForeignKey(Thinktank)
    article = models.ForeignKey(Article)

