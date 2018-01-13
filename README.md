# Basic Flask app with heroku config

Created to have the minimal set of config to be able to run on heroku

## Locally

```bash
pip install gunicorn
gunicorn hello:app
```

## Deploy

Create the heroku app then git push as usual

```bash
heroku create my-flask-app
git push heroku master
```

## Requirements

The requirements.txt file is used by Heroku to know what it needs to install. You can generate your own with a simple:

`pip freeze >> requirements.txt`