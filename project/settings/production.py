import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False

sentry_sdk.init(
    dsn=SENTRY_KEY,
    integrations=[DjangoIntegration()],
    send_default_pii=True,
)
