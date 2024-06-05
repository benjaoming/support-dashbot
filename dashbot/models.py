from django.db import models
from django.utils.text import slugify


class Channel(models.Model):
    channel_type = models.CharField(
        max_length=64,
        choices=[
            ("github", "GitHub"),
            ("help_scout", "HelpScout"),
        ]
    )


class Repository(models.Model):
    url = models.CharField(unique=True, max_length=1024)
    name = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=64)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class IssueTag(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)


class IssueStatus(models.Model):

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)


class Issue(models.Model):
    resolved = models.BooleanField(default=False)
    repository = models.ForeignKey(Repository, on_delete=models.PROTECT, related_name="issues")
    # url = models.URLField(max_length=1024)
    number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=1024)
    github_state = models.CharField(max_length=64)

    tags = models.ManyToManyField(IssueTag)
    status = models.ForeignKey(IssueStatus, on_delete=models.PROTECT, null=True)

    # author = ...

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_url(self):
        return f"{self.repository.url}issues/{self.number}/"


class IssueComment(models.Model):

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    url = models.URLField(max_length=1024)

    by_me = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
