import time
import psutil
from app_logging.log_manager import LogManager


class Monitoring:

    def __init__(self):
        self.logger = LogManager()
        self.running = True

        # 🔥 Live data for Flask dashboard
        self.live_data = {
            "cpu": 0,
            "ram": 0,
            "ram_available": 0,
            "disk": 0
        }

    def monitoring_loop(self):
        self.logger.system("Monitoring started")

        try:
            while self.running:
                # CPU
                cpu = psutil.cpu_percent()

                # RAM
                ram = psutil.virtual_memory().percent
                ram_available = round(
                    psutil.virtual_memory().available / (1024 ** 3), 2
                )

                # Disk
                disk = psutil.disk_usage('/')
                total = round(disk.total / (1024 ** 3), 2)
                used = round(disk.used / (1024 ** 3), 2)
                free = round(disk.free / (1024 ** 3), 2)
                disk_percent = disk.percent

                # 🔥 Update live data (used by Flask API)
                self.live_data["cpu"] = cpu
                self.live_data["ram"] = ram
                self.live_data["ram_available"] = ram_available
                self.live_data["disk"] = disk_percent

                # ✅ REQUIRED OUTPUT FORMAT
                output = (
                    f"CPU Usage: {cpu}%\n"
                    f"RAM Usage: {ram}%\n"
                    f"RAM Available: {ram_available} GB\n"
                    f"Disk | Total: {total} GB | Used: {used} GB | Free: {free} GB"
                )

                # Console
                print(output)
                print("-" * 50)

                # Logs
                self.logger.system(output)

                time.sleep(5)

        except KeyboardInterrupt:
            self.logger.alert("System Resource Monitor stopped by user")
            self.logger.error("Application terminated using KeyboardInterrupt")
            self.running = False


if __name__ == "__main__":
    monitor = Monitoring()

"""""
import time
import psutil
from app_logging.log_manager import LogManager
from alert_decorators import alert_if_exceeds


class Monitoring:

    def __init__(self):
        self.logger = LogManager()
        self.running = True

    @alert_if_exceeds(threshold=80, resource_name="CPU")
    def cpu_monitor(self):
        cpu_usage = psutil.cpu_percent()
        print(f"CPU Usage: {cpu_usage}%")
        self.logger.cpu("CPU Usage", f"{cpu_usage}%")
        return cpu_usage

    @alert_if_exceeds(threshold=75, resource_name="RAM")
    def memory_monitor(self):
        ram_used = psutil.virtual_memory().percent
        print(f"RAM Usage: {ram_used}%")
        self.logger.memory("RAM Usage", f"{ram_used}%")
        return ram_used

    
    def memory_available(self):
        ram_available = psutil.virtual_memory().available / (1024 ** 3)
        print(f"RAM Available: {ram_available:.2f} GB")
        self.logger.memory("RAM Available (GB)", round(ram_available, 2))
        return ram_available

    def disk_monitor(self):
        disk = psutil.disk_usage('/')
        print(
            f"Disk | Total: {disk.total / (1024**3):.2f} GB | "
            f"Used: {disk.used / (1024**3):.2f} GB | "
            f"Free: {disk.free / (1024**3):.2f} GB"
        )
        self.logger.disk("Disk Usage (%)", f"{disk.percent}%")
        return disk.percent

    def monitoring_loop(self):
        self.logger.cpu("Monitoring loop started")
        try:
            while self.running:
                self.cpu_monitor()
                self.memory_monitor()
                self.memory_available()
                self.disk_monitor()
                time.sleep(5)

        except KeyboardInterrupt:
            self.logger.alert("System Resource Monitor stopped by user")
            self.logger.error("Application terminated using KeyboardInterrupt")
            self.running = False


if __name__ == "__main__":
    obj = Monitoring()
    obj.monitoring_loop()
"""