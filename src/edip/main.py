from edip.logging.logger import get_logger
from edip.config.settings import settings


logger=get_logger(__name__)


def main():

    logger.info(
        "Starting Enterprise Data Intelligence Platform"
    )


    logger.info(
        f"Environment: {settings.environment}"
    )


if __name__=="__main__":

    main()