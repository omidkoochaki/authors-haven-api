from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="VoQE5G62Qu1Sk8cmBMa8V8D4nYhWazjaEoH9p9wWGPF4P23A3M68Wtme2BpHSwt",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

