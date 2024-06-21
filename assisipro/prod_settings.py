from decouple import config, Csv
from dj_database_url import parse as db_url
from .settings import *

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=db_url
    )
}