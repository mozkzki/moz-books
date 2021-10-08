import logging
import logging.config
import coloredlogs

# LOG_LEVEL = "DEBUG"
LOG_LEVEL = "INFO"
LOG_FORMAT = "[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": LOG_FORMAT,
                "datefmt": DATE_FORMAT,
            },
        },
        "handlers": {
            "default": {
                "level": LOG_LEVEL,
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
        },
        "loggers": {"": {"handlers": ["default"], "level": LOG_LEVEL, "propagate": True}},
    }
)

coloredlogs.CAN_USE_BOLD_FONT = True
coloredlogs.DEFAULT_FIELD_STYLES = {
    "asctime": {"color": "green"},
    "hostname": {"color": "magenta"},
    "levelname": {"color": "black", "bold": True},
    "name": {"color": "blue"},
    "programname": {"color": "cyan"},
}
coloredlogs.DEFAULT_LEVEL_STYLES = {
    "critical": {"color": "red", "bold": True},
    "error": {"color": "red"},
    "warning": {"color": "yellow"},
    "notice": {"color": "magenta"},
    "info": {},
    "debug": {"color": "black", "bold": True},
    "spam": {"color": "green", "faint": True},
    "success": {"color": "green", "bold": True},
    "verbose": {"color": "blue"},
}


def get_logger(logger_name: str):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(
        level=LOG_LEVEL,
        logger=logger,
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )
    return logger
