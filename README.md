# Real-Time System Resource Monitor

## Project Description
This project is a Python-based system that monitors CPU, memory, and disk usage
in real time and generates alerts and logs to prevent system failures.

## Features
- Continuous system resource monitoring
- Threshold-based alert generation
- File-based logging of resource usage
- Fault-tolerant and scalable design

## System Architecture
The system consists of independent monitoring modules for CPU, memory, and disk,
an alert management module, and a centralized logging system.

## Technologies Used
- Python
- Object-Oriented Programming
- Decorators
- Multithreading
- File Handling
- Exception Handling 

## Folder Structure
- templates/ : Dashboard Frontend And Styling 
- logs/ : Resource and alert logs
- docs/ : Project documentation
- app_logging/ : Log manger which handles file handling

## Real-World Applications
- Server monitoring
- DevOps operations
- System health analysis

## Future Enhancements
- AI-based anomaly detection
- Cloud monitoring support

✨ Features
-Live monitoring of CPU, RAM, and Disk usage
-Real-time data collection using psutil
-Flask-based REST API for serving monitoring data
-Auto-refreshing, responsive web dashboard
-Animated progress bars with color-based alerts
-Background monitoring using multithreading
-JSON-based logging for system metrics and events
-Clean, modular, and scalable project structure

🛠 Tech Stack
-Programming Language: Python
-System Monitoring: psutil
-Backend Framework: Flask
-Frontend: HTML, CSS, JavaScript
-API Communication: REST (JSON)
-Concurrency: Python threading

✅ Conclusion
This project successfully implements a real-time system resource monitoring solution using Python. It captures live CPU, RAM, and Disk metrics with the help of the psutil library and exposes them through a Flask-based REST API. A responsive and professional web dashboard visualizes these metrics with animated progress bars and automatic refresh, providing a clear and intuitive view of system performance.
The project demonstrates practical skills in system monitoring, multithreading, RESTful API development, and front-end integration. Its modular design allows easy extension, such as adding alerts, charts, authentication, or WebSocket-based real-time updates. Overall, this project reflects an industry-oriented approach to building scalable and user-friendly monitoring tools.
