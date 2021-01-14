from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length = 30, null = True) 
    description = models.TextField(max_length = 200, null = True, help_text="Upper Limit : 150 characters") 
    place = models.CharField(max_length = 40, null = True, help_text="City/District, State")
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length = 1000, null = True, blank = True, help_text="Pass the url here")
    
    def __str__(self):
        return f'{self.name} ({self.place})'


class GalleryPhoto(models.Model):
    image_url = models.CharField(max_length = 1000, null = True, help_text="Pass the url here")
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length = 30, null = True) 
    description = models.TextField(max_length = 350, null = True, help_text="Upper Limit : 300 characters") 
    date = models.DateField(auto_now = False, auto_now_add = False, help_text = "YYYY-MM-DD")  
    
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.title} ({self.date})'


class Project(models.Model):
    name = models.CharField(max_length = 30, null = True) 
    description = models.TextField(max_length = 600, null = True, help_text="Upper Limit : 500 characters") 
    date = models.DateField(auto_now = False, auto_now_add = False, help_text = "YYYY-MM-DD")  
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length = 1000, null = True, blank = True, help_text="Pass the url here")
    readMore = models.CharField(max_length = 1000, null = True, blank = True, help_text="Pass the url here")
    
    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f'{self.name} ({self.date})'
