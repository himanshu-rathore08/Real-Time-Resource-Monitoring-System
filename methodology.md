1️⃣ Monitoring Strategy

The system continuously monitors CPU, memory, and disk usage at fixed time intervals. Each resource is monitored independently to avoid performance bottlenecks.

2️⃣ Alert Generation Process

Threshold values are predefined for each system resource. When resource usage exceeds these values, the system generates warning or critical alerts.

3️⃣ Logging Mechanism

System usage data and alerts are logged into separate files with timestamps. This allows easy identification of trends and anomalies.

4️⃣ Multithreading Approach

Separate threads are used for monitoring CPU, memory, and disk usage. This ensures that monitoring remains responsive and efficient.

5️⃣ Exception Handling Strategy

All system-level and runtime errors are captured and logged. The system continues execution even when non-critical errors occur.

6️⃣ Execution Workflow

Initialize system components

Load configuration values

Start monitoring threads

Continuously collect and evaluate data

Log results and alerts