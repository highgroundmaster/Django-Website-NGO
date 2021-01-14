from django.contrib import admin

# Register your models here.
from .models import *
from django.forms import TextInput, Textarea
from django.db import models

class TestimonialAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':7, 'cols':50})},
    }

class GalleryPhotoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':40})},
    }

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':12, 'cols':50})},
    }

admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(GalleryPhoto,GalleryPhotoAdmin)
admin.site.register(Project,ProjectAdmin)