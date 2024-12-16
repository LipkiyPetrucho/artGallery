import os
from .base import *

ENVIRONMENT = os.getenv("DJANGO_ENV", "local")

if ENVIRONMENT == "prod":
    from .prod import *
else:
    from .local import *
