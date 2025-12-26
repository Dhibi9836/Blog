from django.db import models

class About(models.Model) :
    heading = models.CharField(max_length = 25)
    desc = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.heading
    
    class Meta :
        verbose_name_plural = 'about'
        
class SocialLink(models.Model) :
    platform = models.CharField(max_length = 25)
    link = models.URLField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.platform