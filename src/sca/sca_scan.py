import subprocess
import os
import yaml
from utils.logger import logger
import json

# Load configuration
CONFIG_PATH = "config/settings.yaml"

def load_config():
    """Load YAML configuration file."""
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

CONFIG = load_config()

def run_dependency_check():
    """Run OWASP Dependency-Check for SCA."""
    dependency_check_path = "C:/Users/kaytn/dependency-check/bin/dependency-check.bat"  # Update this path
    output_file = CONFIG["sca"]["output_file"]
    scan_target = CONFIG["sca"]["scan_target"]

    if not os.path.exists("reports"):
        os.makedirs("reports")

    try:
        cmd = [
            dependency_check_path,
            "--scan", scan_target,
            "--format", CONFIG["sca"]["report_format"],
            "--out", output_file,
            "--nvdApiKey", CONFIG["sca"]["nvd_api_key"]
        ]

        logger.info(f"Executing: {' '.join(cmd)}")
        subprocess.run(cmd, check=True, shell=True)

        logger.info(f"SCA scan completed. Results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        logger.error(f"SCA scan failed: {e}")

def run_sca_scan():
    """Run Software Composition Analysis (SCA)."""
    if CONFIG["sca"]["enabled"]:
        run_dependency_check()
    else:
        logger.info("SCA is disabled in settings.yaml")

def parse_sca_results():
    """Parse the SCA report and display critical vulnerabilities."""
    report_file = CONFIG["sca"]["output_file"]

    if not os.path.exists(report_file):
        logger.error("SCA report not found.")
        return

    with open(report_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\n📌 **Vulnerability Summary:**\n")
    
    for dependency in data.get("dependencies", []):
        vulnerabilities = dependency.get("vulnerabilities", [])
        if vulnerabilities:
            print(f"🔍 **{dependency.get('fileName', 'Unknown')}**")
            for vuln in vulnerabilities:
                print(f"   - ❌ **{vuln['cve']}** | Severity: {vuln['severity']}")
                print(f"     🔗 {vuln.get('description', 'No details available')}\n")
    
    print("✅ Scan completed. Review the full report for details.")