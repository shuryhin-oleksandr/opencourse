from .base import *  # noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")
ADMIN_URL = env("DJANGO_ADMIN_URL")
