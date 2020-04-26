import logging
import os

from sqlalchemy import create_engine

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        check_db_is_active()
        logger.info("Done")
    except Exception as e:
        logger.error(e)
        raise e


def main():
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


def check_db_is_active():
    USERNAME = os.environ["POSTGRES_USER"]
    PASSWORD = os.environ["POSTGRES_PASSWORD"]
    SERVER = os.environ["POSTGRES_SERVER"]
    engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{SERVER}/airflow")
    engine.connect()
    engine.execute("SELECT 1")


if __name__ == "__main__":
    main()
