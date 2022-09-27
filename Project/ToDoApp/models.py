from django.db import models
from django.urls import reverse
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length =200)
    slug= models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    daycount = models.PositiveIntegerField()
    endgoal = models.CharField(max_length=200)
    due = models.DateTimeField(auto_now_add=False, blank=True, default=datetime.now())

    
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("ToDoApp:details", kwargs={"slug": self.slug})