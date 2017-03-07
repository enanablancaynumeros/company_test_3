from celery.utils.log import get_logger
from db_handlers.utils import get_db_session_scope
from db_handlers.handlers import VisitsHandler
from db_handlers.postgres_config import Postgres_DB_Session
from workers.celery_app import celery_app

logger = get_logger(__name__)


@celery_app.task
def store_gender(info):
    print("Entered the task")
    with get_db_session_scope(Postgres_DB_Session) as db_session:
        visit_handler = VisitsHandler(db_session)
        logger.info("Adding record for client {}".format(info["client_id"]))
        visit_handler.add(**info)
        logger.info("Updated record for client {}".format(info["client_id"]))
