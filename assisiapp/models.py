from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify



class Saints_Model(models.Model): 
    name = models.CharField(max_length=100)
    quotes = models.CharField(max_length=1000)
    saint_image = models.ImageField(upload_to='images/')
    date = models.DateTimeField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        return self.date >= timezone.now()

class Provinical_Administration(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class News_Category(models.Model):
    news_heading = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.news_heading

class Latest_News_Model(models.Model):
    category = models.ForeignKey(News_Category,on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    news_images = models.ImageField(upload_to='images/',null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.news_heading


# class Event_Categoty(models.Model):
#     event_name = models.CharField(max_length=100)
#     event_start_date = models.DateField()
#     event_end_date = models.DateTimeField()
#     status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    
#     def is_active(self):
#         return self.event_end_date >= timezone.now()

    
# class Event_Model(models.Model):
#     category = models.ForeignKey(Event_Categoty,on_delete=models.CASCADE)
#     organizer = models.CharField(max_length=100)
#     event_description = models.CharField(max_length=1000)
#     end_date = models.DateTimeField()
#     end_time = models.TimeField()
#     event_venue = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     event_image = models.ImageField(upload_to='images/')
#     status = models.BooleanField(default=False,help_text="0-default,1-Hidden")


class GalleryModel(models.Model):
    gallery_image = models.ImageField(upload_to='images/')


class Event_Details(models.Model):
    event_name = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100,null=True,blank=True)
    event_description = models.CharField(max_length=5000,null=True,blank=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateTimeField()
    end_time = models.TimeField(null=True,blank=True)
    event_venue = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=10, null=True,blank=True)
    website_link = models.CharField(max_length=200,null=True,blank=True)
    event_image = models.ImageField(upload_to='images/',null=True,blank=True)

    def is_active(self):
        return self.end_date >= timezone.now()
    
    def __str__(self):
        return self.event_name


class EnquiryModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200,null=True,blank=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class FriarsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image  = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Obituary_Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Wishes(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    heading = models.CharField(max_length=200)
    wishes = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=100,null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Provincial_administation(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Telengana_delegation(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kolkata_Mission(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Srilankan_Mission(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class About_Model(models.Model):
  About_video = models.URLField(max_length=200, unique=True, null=True, blank=True)

  def __str__(self):
    return self.About_video

class VideoGallery(models.Model):
    video_gallery = models.URLField(max_length=300, unique=True, null=True, blank=True)
    video_name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.video_gallery

class NoticeModel(models.Model):
    heading = models.CharField(max_length=200)
    main_description = models.CharField(max_length=300, null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
    organizer = models.CharField(max_length=100, null=True, blank=True) 
    description = models.CharField(max_length=1000, null=True,blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.heading