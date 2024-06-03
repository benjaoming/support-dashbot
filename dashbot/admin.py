from django.contrib import admin

from . import models


@admin.register(models.Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):
    pass
