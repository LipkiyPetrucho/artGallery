import os
from .settings import *

ENVIRONMENT = os.getenv("DJANGO_ENV")

if ENVIRONMENT == "prod":
    from .prod import *
else:
    from .local import *
