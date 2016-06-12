from django.contrib import admin

from logistic import models

admin.site.register(models.SimpleRequestModel)
admin.site.register(models.RequestModel)
