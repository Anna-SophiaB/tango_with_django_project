from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    MAX_LENGTH_NAME = 128

    name = models.CharField(max_length=MAX_LENGTH_NAME, unique = True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    MAX_LENGTH_TITLE = 128
    MAX_LENGTH_URL = 200

    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    #This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        # returns meaningful value when string representaion of
        # UserProfile model is requested.
        return self.user.username















    