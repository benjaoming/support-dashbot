from django.conf import settings
from django.core.management.base import BaseCommand

from ... import models
from ... import service

class Command(BaseCommand):
    help = "Remember to update issues before triaging."

    def handle(self, *args, **options):
        repository, __ = models.Repository.objects.get_or_create(
            name=settings.GITHUB_REPO,
            defaults={
                "url": f"https://github.com/{settings.GITHUB_REPO}/",
            }
        )

        g_repo = service.get_repo(repository)

        for issue in models.Issue.objects.filter(github_state="open"):
            g_issue = g_repo.get_issue(number=issue.number)
            print(f"Triaging {issue.number}.. adding a comment")
            g_issue.create_comment("The bot was here to triage!")
