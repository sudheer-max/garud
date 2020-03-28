from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Domestic_city(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Domestic_inclusion(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Domestic(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(default="this is short overview of the package")
    thumbnail = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, default="Number of Days/Nigths  of the packages")
    featured = models.BooleanField()
    cities = models.ManyToManyField(Domestic_city)
    inclusiones = models.ManyToManyField(Domestic_inclusion)
    content = RichTextUploadingField(default="this is a table editor of the current packages")
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('umesh:domestic-detail', kwargs= {
            'slug' : self.slug
        })


class International_city(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class International_inclusion(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class International(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(default="this is short overview of the package")
    thumbnail = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, default="Number of Days/Nigths  of the packages")
    featured = models.BooleanField()
    cities = models.ManyToManyField(International_city)
    inclusiones = models.ManyToManyField(International_inclusion)
    content = RichTextUploadingField(default="this is a table editor of the current packages")
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('umesh:international-detail', kwargs = {
            'slug' : self.slug
        })


class Hotel_city(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Hotel_inclusion(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(default="this is short overview of the package")
    thumbnail = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, default="Number of Days/Nigths  of the packages")
    featured = models.BooleanField()
    cities = models.ManyToManyField(Hotel_city)
    inclusiones = models.ManyToManyField(Hotel_inclusion)
    content = RichTextUploadingField(default="this is a table editor of the current packages")
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('umesh:hotel-detail', kwargs = {
            'slug' : self.slug
        })
    
class Bus(models.Model):
    thumbnail = models.ImageField(upload_to='')
    bus_name = models.CharField(max_length=50)
    ac_rate = models.IntegerField(default=0)
    non_rate = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    allowance = models.IntegerField(default=0)
    night_allowance = models.IntegerField(default=0)
    featured = models.BooleanField()

    def __str__(self):
        return self.bus_name

class Car(models.Model):
    thumbnail = models.ImageField(upload_to='')
    car_name = models.CharField(max_length=50)
    ac_rate = models.CharField(max_length=50)
    extra_person = models.CharField(max_length=50)
    extra_hour = models.CharField(max_length=50)
    nigth_allowance = models.CharField(max_length=50)
    featured = models.BooleanField()


    def __str__(self):
        return self.car_name


class Testimonial(models.Model):
    thumbnail = models.ImageField(upload_to='')
    overview = models.TextField(default="this is testimonial field of the satisfied customers.")
    title = models.CharField(max_length=50)
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Header(models.Model):
    thumbnail = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=50)
    featured = models.BooleanField()

    def __str__(self):
        return self.title