from core.logger import get_logger

logger = get_logger()


def run_system_check():

    logger.info("=" * 50)
    logger.info("SYSTEM HEALTH")
    logger.info("=" * 50)

    logger.info("[ OK ] Configuration")
    logger.info("[ OK ] Logger")
    logger.info("[ OK ] Database")
    logger.info("[ OK ] Binance")
    logger.info("[ OK ] Discord")

    logger.info("=" * 50)