# 🚀 Automated Root Cause Analysis (RCA) & Monitoring System

## 📌 Overview
An end-to-end event-driven monitoring and automated Root Cause Analysis (RCA) system. This project simulates a production DevOps environment where a microservice is continuously monitored. Upon detecting a failure, the system automatically triggers an RCA engine to collect system metrics, analyze Docker container states, and generate a remediation report to reduce Mean Time To Recovery (MTTR).

## 🛠️ Tech Stack & DevOps Practices
* **Infrastructure:** Linux (Ubuntu)
* **Scripting & Automation:** Python 3, Bash/Shell (`subprocess`)
* **Containerization:** Docker
* **Continuous Integration (CI):** Jenkins (Pipeline-as-Code with `Jenkinsfile`)
* **Version Control:** Git & GitHub

## ⚙️ Core Features
1. **Active Monitoring:** A Python daemon continuously polls the target application's health endpoint.
2. **Automated Incident Response:** Upon failure detection (Connection Refused / Timeout), the RCA engine is instantly triggered.
3. **Diagnostic Data Collection:** Automatically runs native Linux commands (`free -m`, `df -h`) and Docker commands to gather host and container metrics.
4. **Rule-Based RCA Analysis:** Parses logs and metrics against predefined thresholds to hypothesize root causes (e.g., Out-Of-Memory, Container Crash) and prescribes explicit CLI commands to fix the issue.
5. **CI/CD Pipeline:** Automated syntax checking and Docker image building upon every push to the repository via Jenkins.

## 🧪 Chaos Engineering Demo
To test the resilience of the system:
1. Start the monitoring engine: `python3 rca_engine/monitor.py`
2. Manually assassinate the container: `docker stop target-app`
3. The monitor will catch the failure, trigger the collector, and save an automated incident report in `rca_engine/incident_reports/` detailing the exact cause and the suggested `docker restart` fix.