from django.contrib import admin
from . models import AppUsers, Posts, Work, Projects, ActivityImages


admin.site.register(AppUsers)
admin.site.register(Posts)
admin.site.register(Work)
admin.site.register(Projects)
admin.site.register(ActivityImages)