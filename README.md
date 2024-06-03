# support-dashbot (prototype)
A bot and a dashboard to assist with support via GitHub repositories.

The purpose is to:

* Assist with triaging support issues (bot)
* Configure and experiment with different behavior (bot)
* Actionable daily overview for support worker (dashboard)
* Key metrics for support activities (dashboard)

## Prerequisites

* A GitHub repo + GitHub App configured with access to write issue comments and fetch info via API

## Other trajectories

Through webhook callbacks, it's possible to maintain a live overview in the Dashboard and possibly alert other channels (Zulip, Slack etc).

## Development

```
pip install -r requirements.txt

# Edit local.py
# See settings template below
nano project/settings/local.py

# Bootstrap database
python manage.py migrate

# Add a user
python manage.py createsuperuser

# Collect issue information from repo
python manage.py update_issues

# Triage issues. Default: Dry-run
python manage.py triage_issues --oldest --count=10

# Run project's web interface and webhook locally
python manage.py runserver
```

### Settings template

```
GITHUB_REPO = "benjaoming/support-dashbot"
GITHUB_APP_ID = "123456"
GITHUB_APP_PRIVATE_KEY = """{insert .pem file from GitHub}"""
```

## Usage

The project is deployed to a demo here:

...
