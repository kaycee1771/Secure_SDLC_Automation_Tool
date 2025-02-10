import sys
import os
import subprocess
from utils.logger import logger
import yaml

# Load configuration
CONFIG_PATH = "config/settings.yaml"

def load_config():
    """Load YAML configuration file."""
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

CONFIG = load_config()

def generate_threat_model():
    """Call `run_pytm.py` in a clean subprocess to avoid import conflicts."""
    logger.info("🔍 Starting Threat Model Generation...")

    output_file = CONFIG["threat_modeling"]["output_file"]

    if not os.path.exists("reports"):
        os.makedirs("reports")

    logger.info("📌 Running Threat Model Analysis via Separate Process...")

    try:
        # ✅ Run `run_pytm.py` instead of calling pytm directly
        script_path = os.path.join(os.path.dirname(__file__), "run_pytm.py")
        result = subprocess.run(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Capture and log any errors
        if result.stdout.strip():
            logger.info(f"✅ Threat Modeling Output:\n{result.stdout}")
        else:
            logger.error("❌ Error: Threat Model report is empty! Check pytm output.")

        logger.info(f"✅ Threat Modeling completed. Report saved to {output_file}")
    except Exception as e:
        logger.error(f"❌ Error executing Threat Modeling: {e}")

def run_threat_modeling():
    """Execute Threat Modeling."""
    logger.info("🚀 Running Threat Modeling...")
    generate_threat_model()
    logger.info("🏁 Threat Modeling Execution Finished.")
