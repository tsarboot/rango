from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(blank=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta():
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Car(models.Model): 
    category = models.ForeignKey(Category,on_delete=models.CASCADE,help_text="you should know the car category before buying it ")
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
class UserProfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profil_images',blank=True)
    def __str__(self):
        return self.user.username
