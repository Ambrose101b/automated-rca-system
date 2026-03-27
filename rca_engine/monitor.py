import requests
import time
import os
from collector import collect_metrics  # Importing our data collector!

TARGET_URL = "http://127.0.0.1:5000/health"
LOG_DIR = "incident_reports"

# Create a folder to store our RCA reports if it doesn't exist yet
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def trigger_rca(error_message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] TRIGGERING AUTOMATED RCA...")
    
    # Call the function from collector.py
    report = collect_metrics()
    
    # Add the reason for the crash to the top of the report
    full_report = f"INCIDENT REASON: {error_message}\n{report}"
    
    # Create a unique filename based on the exact time of the crash
    filename = f"{LOG_DIR}/rca_report_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Save the report to a file
    with open(filename, "w") as file:
        file.write(full_report)
        
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] RCA Report successfully saved to {filename}")

def check_health():
    try:
        response = requests.get(TARGET_URL, timeout=5)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] OK: Service is healthy.")
        else:
            error_msg = f"App returned status code {response.status_code}"
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] WARNING: {error_msg}")
            trigger_rca(error_msg)
            
    except requests.exceptions.RequestException as e:
        error_msg = f"Service Connection Refused"
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] CRITICAL: {error_msg}")
        trigger_rca(error_msg)

if __name__ == '__main__':
    print("Starting RCA Monitor...")
    while True:
        check_health()
        time.sleep(5) # Wait 5 seconds between checks