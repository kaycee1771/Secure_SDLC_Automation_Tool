import sys
import os
import argparse
from utils.logger import logger
from sast.sast_scan import run_sast_scan
from sca.sca_scan import run_sca_scan
from threat_modeling.threat_model import run_threat_modeling
from merge_reports import merge_reports

def main():
    parser = argparse.ArgumentParser(description="Secure SDLC Automation Tool")
    parser.add_argument("--sast", action="store_true", help="Run Static Application Security Testing")
    parser.add_argument("--sca", action="store_true", help="Run Software Composition Analysis")
    parser.add_argument("--threat-model", action="store_true", help="Run Automated Threat Modeling")  # ✅ Correct Argument

    args = parser.parse_args()

    logger.info(f"🛠 Arguments Received: {args}")

    if args.sast:
        logger.info("🚀 Running SAST scan...")
        run_sast_scan()

    if args.sca:
        logger.info("🚀 Running SCA scan...")
        run_sca_scan()

    if args.threat_model:
        logger.info("🚀 Running Threat Modeling...")
        run_threat_modeling()

if __name__ == "__main__":
    logger.info("🔧 Secure SDLC Automation Tool Started!")
    main()
    logger.info("✅ Secure SDLC Automation Tool Finished!")
