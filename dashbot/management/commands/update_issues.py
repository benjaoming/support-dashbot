from django.conf import settings
from django.core.management.base import BaseCommand

from ... import models
from ... import service

class Command(BaseCommand):
    help = "Fetches new data from GitHub. Run periodically!"

    def handle(self, *args, **options):
        repository, __ = models.Repository.objects.get_or_create(
            name=settings.GITHUB_REPO,
            defaults={
                "url": f"https://github.com/{settings.GITHUB_REPO}/"
            }
        )

        g_repo = service.get_repo(repository)
        for g_issue in g_repo.get_issues():
            issue, __ = models.Issue.objects.get_or_create(
                repository=repository,
                number=g_issue.number,
            )

            issue.title = g_issue.title
            issue.github_state = g_issue.state

            issue.save()

