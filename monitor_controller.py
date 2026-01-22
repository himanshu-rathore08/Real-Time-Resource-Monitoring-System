import threading
import time

from app_logging.log_manager import LogManager
from monitoring import Monitoring
from exception_handler import handle_exception


class MonitorController:

    def __init__(self):
        self.logger = LogManager()
        self.monitor = Monitoring()
        self.threads = []
        self.running = False

    def start_monitors(self):
        # ✅ FIXED
        self.logger.system("Initializing monitor controller")

        try:
            self.running = True

            cpu_thread = threading.Thread(
                target=self.monitor.cpu_monitor,
                name="CPU-Monitor",
                daemon=True
            )

            memory_thread = threading.Thread(
                target=self.monitor.memory_monitor,
                name="Memory-Monitor",
                daemon=True
            )

            memory_available_thread = threading.Thread(
                target=self.monitor.memory_available,
                name="Memory-Available",
                daemon=True
            )

            disk_thread = threading.Thread(
                target=self.monitor.disk_monitor,
                name="Disk-Monitor",
                daemon=True
            )

            self.threads.extend([
                cpu_thread,
                memory_thread,
                memory_available_thread,
                disk_thread
            ])

            for thread in self.threads:
                thread.start()
                print(f"Thread running: {thread.name} | Alive: {thread.is_alive()}")

            # ✅ FIXED
            self.logger.system("All monitors started successfully")

        except Exception as e:
            handle_exception(e, "MonitorController.start_monitors")

    def keep_alive(self):
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_monitors()

    def stop_monitors(self):
        self.running = False
        self.logger.alert("Stopping all monitors")
        self.logger.error("Monitoring stopped by user")


if __name__ == "__main__":
    controller = MonitorController()
    controller.start_monitors()
    controller.keep_alive()

"""""
import threading
import time

from app_logging.log_manager import LogManager
from monitoring import Monitoring
from exception_handler import handle_exception


class MonitorController:

    def __init__(self):
        self.logger = LogManager()
        self.monitor = Monitoring()   
        self.threads = []
        self.running = False

    def start_monitors(self):
        self.logger.cpu("Initializing monitor controller")

        try:
            self.running = True

            cpu_thread = threading.Thread(
                target=self.monitor.cpu_monitor,
                name="CPU-Monitor",
                daemon=True
            )

            memory_thread = threading.Thread(
                target=self.monitor.memory_monitor,
                name="Memory-Monitor",
                daemon=True
            )

            memory_available_thread = threading.Thread(
                target=self.monitor.memory_available,
                name="Memory-Available",
                daemon=True
            )

            disk_thread = threading.Thread(
                target=self.monitor.disk_monitor,
                name="Disk-Monitor",
                daemon=True
            )

            self.threads.extend([
                cpu_thread,
                memory_thread,
                memory_available_thread,
                disk_thread
            ])

            for thread in self.threads:
                thread.start()
                print(f"Thread running: {thread.name} | Alive: {thread.is_alive()}")
                print("Active threads:", threading.active_count())

            self.logger.cpu("All monitors started successfully")

        except Exception as e:
            handle_exception(e, "MonitorController.start_monitors")

    def keep_alive(self):
        try:
            while self.running:
                time.sleep(1)

        except KeyboardInterrupt:
            self.stop_monitors()

    def stop_monitors(self):
        self.running = False
        self.logger.alert("Stopping all monitors")
        self.logger.error("Monitoring stopped by user")
if __name__ == "__main__":
    controller = MonitorController()
    controller.start_monitors()
"""""