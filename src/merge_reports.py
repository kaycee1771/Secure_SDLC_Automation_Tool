import json
import os

# Define paths for the reports
REPORTS_DIR = "reports"
BANDIT_REPORT = "C:/Users/kaytn/secure_sdlc_automation/reports/bandit_report.json"
SCA_REPORT = "C:/Users/kaytn/secure_sdlc_automation/reports/sca_report.json"
THREAT_MODEL_REPORT = "C:/Users/kaytn/secure_sdlc_automation/reports/threat_model_report.txt"
FINAL_REPORT = "C:/Users/kaytn/secure_sdlc_automation/reports/final_security_report.json"

def load_json_report(file_path):
    """Load a JSON report file if it exists, else return an empty dict."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"⚠️ Warning: Unable to parse JSON from {file_path}")
            return {}
    return {}

def load_text_report(file_path):
    """Load a text-based threat model report."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Threat Model Report Not Found"

def merge_reports():
    """Merge all available reports into one final JSON report."""
    print("🔄 Merging security reports...")

    final_report = {
        "sast_bandit": load_json_report(BANDIT_REPORT),
        "sca_dependency_check": load_json_report(SCA_REPORT),
        "threat_modeling": load_text_report(THREAT_MODEL_REPORT)
    }

    with open(FINAL_REPORT, "w", encoding="utf-8") as file:
        json.dump(final_report, file, indent=4)

    print(f"✅ Final security report saved: {FINAL_REPORT}")

if __name__ == "__main__":
    merge_reports()
