import subprocess
import os
from utils.logger import logger

def run_bandit():
    """Run Bandit for Python security scanning."""
    output_file = "reports/bandit_report.json"

    if not os.path.exists("reports"):
        os.makedirs("reports")

    try:
        cmd = ["bandit", "-r", "src", "-f", "json", "-o", output_file]
        logger.info(f"Executing: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

        logger.info(f"Bandit scan completed. Results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Bandit scan failed: {e}")

def run_sast_scan():
    """Run SAST scan using Bandit."""
    run_bandit()
