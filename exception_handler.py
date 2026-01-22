from app_logging.log_manager import LogManager
import traceback

logger=LogManager()

def handle_exception(exception , source="Unknown"):
    error_message = f"Exception in {source}: {str(exception)}"
    logger.error(error_message)