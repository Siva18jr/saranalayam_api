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
    image = models.TextField()
    postedCategory = models.CharField(max_length=50, null=False, blank=False)
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
    

class Work(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    startDate = models.CharField(max_length=20, null=False, blank=False)
    startTime = models.CharField(max_length=20, null=False, blank=False)
    endDate = models.CharField(max_length=20, null=False)
    endTime = models.CharField(max_length=20, null=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.startTime
    

class Projects(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class ActivityImages(models.Model):
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url