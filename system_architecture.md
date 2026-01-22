1️⃣ System Overview

The Real-Time System Resource Monitoring System follows a modular and layered architecture to ensure scalability, maintainability, and fault tolerance. Each component of the system is responsible for a specific task, following the principle of separation of concerns.

2️⃣ Architectural Components

The system is divided into the following major components:

🔹 Resource Monitoring Modules

CPU Monitoring Module

Memory Monitoring Module

Disk Monitoring Module

Each module is responsible for collecting real-time usage data of a specific system resource.

🔹 Alert Management Module

This module evaluates monitored values against predefined threshold limits and determines whether an alert should be generated.

🔹 Logging Module

The logging module records system usage data, alerts, and errors into structured log files for future analysis and troubleshooting.

🔹 Controller Module

The controller manages the lifecycle of the monitoring system, including initialization, thread management, and graceful shutdown.

3️⃣ Data Flow Explanation

Resource modules collect usage data

Collected data is passed to the alert module

Alert module evaluates threshold conditions

Logging module records usage and alerts

Controller ensures continuous execution

4️⃣ Architectural Advantages

Modular design

Easy scalability

Fault tolerance

Industry-aligned system structure