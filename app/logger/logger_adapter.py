import logging
import watchtower
from boto3.session import Session
from logging import config

from app.core.config import settings
from app.utils import SingletonMeta

REC_ENV = settings.REC_ENV
AWS_REGION_NAME = settings.AWS_REGION_NAME
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY

log_config = settings.LOGGER_CONFIG
print(logging.__file__)
config.dictConfig(log_config)


class FALoggerAdapter(metaclass=SingletonMeta):
    def __init__(self, app_name, logger_name):
        if REC_ENV != 'local':
            boto3_session = Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name=AWS_REGION_NAME
            )

            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger('watchtower')
            self.logger.addHandler(
                watchtower.CloudWatchLogHandler(
                    log_group='fastapi',
                    stream_name=f'logs-{REC_ENV}',
                    boto3_session=boto3_session
                )
            )
        else:
            logging.basicConfig(level=logging.INFO)
            # Initial construct.
            self.app_name = app_name
            # Complete logging config.
            self.logger = logging.getLogger(logger_name)

    def construct_extra(self, msg=None, track=None, extra: dict = None):
        rtn_extra = {
            "app": self.app_name,
            "message": msg,
        }
        if track:
            rtn_extra.update({"track": track})
        if extra:
            rtn_extra.update({"props": extra})
        return rtn_extra

    def info(self, msg, track=None, extra: dict = None):
        extra = self.construct_extra(msg, track, extra)
        self.logger.info(extra)

    def error(self, msg, track=None, extra: dict = None):
        extra = self.construct_extra(msg, track, extra)
        self.logger.error(extra)

    def debug(self, msg, track=None, extra: dict = None):
        extra = self.construct_extra(msg, track, extra)
        self.logger.debug(extra)

    def warning(self, msg, track=None, extra: dict = None):
        extra = self.construct_extra(msg, track, extra)
        self.logger.warning(extra)

    def log(self, msg, track=None, extra: dict = None):
        extra = self.construct_extra(msg, track, extra)
        self.logger.log(level=logging.INFO, msg=msg)


logger = FALoggerAdapter("Candidates Ranking Microservice", "watchtower")
