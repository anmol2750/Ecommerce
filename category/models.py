from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True, blank = False)
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
