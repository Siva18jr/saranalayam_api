from django.db import models


class AppUsers(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=70, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    token = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username
    

class Posts(models.Model):
    projectName = models.CharField(max_length=50, null=False, blank=False)
    postedUser = models.CharField(max_length=50, null=False, blank=False)
    postedAt = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url