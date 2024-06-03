from django.shortcuts import render

from . import models


# TODO: Support multiple repos, redirect to slug of first one
def index(request):
    repository = models.Repository.objects.all()[0]
    return render(
        request,
        template_name="dashbot/index.html",
        context={
            "repository": repository,
            "issues_open": models.Issue.objects.filter(repository=repository, github_state="open")
        }
    )



# TODO: Support multiple repos, redirect to slug of first one
def todo(request):
    repository = models.Repository.objects.all()[0]
    return render(
        request,
        template_name="dashbot/todo.html",
        context={
            "repository": repository,
            "issues_open": models.Issue.objects.filter(repository=repository, github_state="open")
        }
    )
