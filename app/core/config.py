import logging
import os
from distutils.util import strtobool
from pathlib import Path

from pydantic import BaseSettings, EmailStr

APP_NAME = os.environ.get("APP_NAME", "micro_template")
DEBUG = strtobool(os.environ.get("DEBUG", "False"))

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "PvgAYV-2L258hP633qxXDqx0r8xjiIITta29oB9sBiYPCR1IhtrJ7w")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 90
    APP_NAME: str = APP_NAME
    DEBUG: bool = DEBUG
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    LOGGER_CONFIG: dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(name)-12s %(levelname)-8s %(message)s'
            },
            'file': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'file',
                'filename': os.path.join('/logs', f'{APP_NAME}.log'),
                'when': 'midnight',
                'interval': 1,
                'backupCount': 15
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            },
            'gunicorn.glogging.Logger': {
                'level': 'INFO',
                'handlers': ['console']
            },
            'celery': {
                'handlers': ['console'],
                'level': 'INFO'
            }
        }
    }
    REC_ENV: str

    # DB
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    ENABLE_FUNCTIONALITY: tuple = (True, "Functionality is activated")
    BASE_URL_FASTAPI: str

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    class Config:
        env_file = "..env"

    def __init__(self, *args, **kwargs):
        if not os.path.exists('logs'):
            os.mkdir('logs')

        log_file = os.path.join('logs', f'{APP_NAME}.log')

        if not os.path.exists(log_file):
            Path(log_file).touch()

        super(Settings, self).__init__(*args, **kwargs)


settings = Settings()

CITIES = {
    'cali,colombia': [3.451647, -76.531982],
    'bogota,colombia': [4.710989, -74.072090],
    'medellin,colombia': [6.244203, -75.581215],
    'barranquilla,colombia': [10.963889, -74.796387],
    'pereira,colombia': [4.81333, -75.69611],
    'santiago,chile': [-33.448891, -70.669266],
    'bahia blanca,argentina': [-38.718319, -62.266350],
    'asuncion,paraguay': [-25.26374, -57.575926],
    'la paz,bolivia': [-16.489689, -68.119294],
    'buenos aires,argentina': [-34.603722, -58.381592],
    'caba,argentina': [-34.603722, -58.381592],
    'cordoba,argentina': [-31.416668, -64.183334],
    'la plata,argentina': [-34.920345, -57.969559],
    'mar del plata, argentina': [-37.979858, -57.589794],
    'mendoza,argentina': [-32.888355, -68.838844],
    'resistencia,argentina': [-27.451862, -58.985555],
    'rosario,argentina': [-32.950001, -60.666668],
    'tandil,argentina': [-37.320480, -59.132904],
    'tucuman,argentina': [-26.808285, -65.217590],
    'sao jose,brazil': [-28.21171, -49.1632],
    'sao paulo,brazil': [-23.533773, -46.625290],
    'san jose, costa rica': [9.934739, -84.087502],
    'quito,ecuador': [-0.22985, -78.52495],
    'lima,peru': [-12.046374, -77.042793],
    'arequipa,peru': [-16.409047, -71.537451],
    'montevideo,uruguay': [-34.901112, -56.164532],
    'ciudad de mexico,mexico': [19.432608, -99.133209],
    'guadalajara,mexico': [20.659698, -103.349609],
    'monterrey,mexico': [25.686613, -100.316116],
    'los angeles,usa': [34.052235, -118.243683],
    'miami,usa': [25.761681, -80.191788],
    'new york,usa': [40.730610, -73.935242],
    'raleigh,usa': [35.787743, -78.644257],
    'san francisco,usa': [37.773972, -122.431297],
    'seattle,usa': [47.608013, -122.335167],
    'minsk,belarus': [53.893009, 27.567444],
    'barcelona,spain': [41.390205, 2.154007],
    'berlin,germany': [52.520008, 13.404954],
    'madrid,spain': [40.416775, -3.703790],
    'malaga,spain': [36.719444, -4.420000],
    'paris,france': [48.864716, 2.349014],
    'luxembourg': [49.611622, 6.131935],
    'cluj-napoca,romania': [46.770439, 23.591423],
    'london,united kingdom': [51.509865, -0.118092],
    'bangalore,india': [12.972442, 77.580643],
    'pune,india': [18.516726, 73.856255]
}  # lat-long
