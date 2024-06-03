from django.conf import settings

from github import GithubIntegration

# Authentication is defined via github.Auth
from github import Auth

from . import models


def get_repo(repository: models.Repository):
    # using an access token
    auth = Auth.AppAuth(app_id=settings.GITHUB_APP_ID, private_key=settings.GITHUB_APP_PRIVATE_KEY)

    # Authenticate the app, figure out where it's installed and fetch an authentication
    # token for a particular installation.
    # TODO: We should really match the repo name here...
    g = GithubIntegration(auth=auth).get_installations()[0].get_github_for_installation()

    return g.get_repo(repository.name)
