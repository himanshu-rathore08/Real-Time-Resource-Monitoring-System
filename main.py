import time,os,threading
from app_logging.log_manager import LogManager
from monitoring import Monitoring
from monitor_controller import MonitorController
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    logger = LogManager()
    obj = Monitoring()
    obj.monitoring_loop()
    controller = MonitorController()
    controller.start_monitors()
    controller.keep_alive()
   
    logger.system("System Resource Monitor started")

    try:
        while True:
            time.sleep(5)
            
           
    except KeyboardInterrupt:
        logger.alert("System Resource Monitor stopped by user")
        logger.error("Application terminated using KeyboardInterrupt")

if __name__ == "__main__":
    main()
