
from decouple import config


if config('PRODUCTION_ENV', default=False, cast=bool):
    from .config.production_env import *
else:
    from .config.local_env import *
