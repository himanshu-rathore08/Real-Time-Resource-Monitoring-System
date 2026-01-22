import os
import json
from datetime import datetime


class LogManager:

    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, "system_monitor.json")

    def write(self, level, message: str):
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level,
            "log": message
        }

        with open(self.log_file, "a", encoding="utf-8") as f:
            json.dump(log_entry, f)
            f.write("\n\n")

    def system(self, message: str):
        self.write("SYSTEM", message)

    def alert(self, message: str):
        self.write("ALERT", message)

    def error(self, message: str):
        self.write("ERROR", message)

if __name__ == "__main__":
    logger = LogManager()
    logger.alert("High CPU usage detected")
    logger.error("Disk read failed")        



"""""
import os
import json
from datetime import datetime


class LogManager:

    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, "system_monitor.json")

    def _write(self, level, message, value=None):
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level,
            "message": message
        }

        if value is not None:
            log_entry["value"] = value

        with open(self.log_file, "a", encoding="utf-8") as f:
            json.dump(log_entry, f)
            f.write("\n\n")

    # ✅ UPDATED METHODS
    def cpu(self, message, value=None):
        self._write("CPU", message, value)

    def memory(self, message, value=None):
        self._write("MEMORY", message, value)

    def disk(self, message, value=None):
        self._write("DISK", message, value)

    def alert(self, message):
        self._write("ALERT", message)

    def error(self, message):
        self._write("ERROR", message)

if __name__ == "__main__":
    logger = LogManager()
    logger.cpu("CPU Usage", "66.7%")
    logger.memory("RAM Usage", "75.6%")
    logger.disk("Disk Usage", "70%")
    logger.alert("High CPU usage detected")
    logger.error("Disk read failed")
"""