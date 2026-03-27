import subprocess
import time

def collect_metrics():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Initiating RCA System Data Collection...")
    
    # 1. Gather Host Metrics
    memory_usage = subprocess.getoutput("free -m")
    disk_usage = subprocess.getoutput("df -h /")
    
    # 2. Gather Docker Metrics (New!)
    # Check if target-app is running or exited
    docker_status = subprocess.getoutput("docker ps -a -f name=target-app --format '{{.Status}}'")
    # Grab the last 5 lines of the container's logs to see why it crashed
    docker_logs = subprocess.getoutput("docker logs --tail 5 target-app 2>&1")
    
    # 3. --- RULE-BASED ANALYSIS (The Brain) ---
    analysis_results = []
    
    # Rule 1: Is the container dead?
    if "Exited" in docker_status or not docker_status.strip():
        analysis_results.append("❌ ROOT CAUSE: The Docker container 'target-app' has crashed or stopped.")
        analysis_results.append("💡 SUGGESTED FIX: Restart the container using command: `docker restart target-app`")
    else:
        analysis_results.append("✅ Container status is active. Crash might be a network or code freeze issue.")
        
    # Rule 2: Is the disk completely full?
    if "100%" in disk_usage or "99%" in disk_usage:
        analysis_results.append("❌ ROOT CAUSE: Host disk space is critically full.")
        analysis_results.append("💡 SUGGESTED FIX: Free up space by removing old logs or unused Docker images (`docker image prune`).")

    # Format the rules output
    analysis_text = "\n".join(analysis_results)

    # Combine everything into our final report
    report = f"""
=== RCA METRICS & ANALYSIS REPORT ===
Time: {time.strftime('%Y-%m-%d %H:%M:%S')}

--- 🤖 AUTOMATED ANALYSIS & FIXES ---
{analysis_text}

--- 🐳 DOCKER CONTAINER LOGS ---
{docker_logs if docker_logs else "No logs found."}

--- 💻 HOST SYSTEM METRICS ---
[Memory]
{memory_usage}

[Disk]
{disk_usage}
=====================================
    """
    
    return report

if __name__ == '__main__':
    # Test the function manually
    print(collect_metrics())