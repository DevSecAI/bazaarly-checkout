# BAZ-SAST-004 / BAZ-SAST-005: hardcoded secrets, DEBUG enabled, ALLOWED_HOSTS=*.
SECRET_KEY = "django-insecure-bazaarly-9F2B7E1A-do-not-rotate"
STRIPE_SECRET_KEY = "sk_live_BENCH_PLACEHOLDER_NOT_REAL"

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bazaarly",
        "USER": "bazaarly",
        "PASSWORD": "ChangeMe2024!",
        "HOST": "bazaarly-prod.cloudsql.example",
        "PORT": "5432",
    }
}

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages",
    "bazaarly.orders", "bazaarly.marketing", "bazaarly.auth",
]
ROOT_URLCONF = "bazaarly.urls"
WSGI_APPLICATION = "bazaarly.wsgi.application"
