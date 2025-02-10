import sys
import subprocess
import os
import io

# Force UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

def run_pytm():
    """Execute pytm with a defined threat model."""
    report_file = "reports/threat_model_report.txt"

    try:
        print("🔍 Running pytm with a threat model...")

        # Run pytm_script.py, which explicitly defines a threat model
        script_path = os.path.join(os.path.dirname(__file__), "pytm_script.py")
        result = subprocess.run(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print raw output for debugging
        print("⚠️ Pytm Output:\n", result.stdout)
        print("⚠️ Pytm Errors:\n", result.stderr)

        if not result.stdout.strip():
            print("❌ Error: Pytm output is empty. Check pytm execution.", flush=True)
            return

        # Save to report file
        with open(report_file, "w", encoding="utf-8") as file:
            file.write(result.stdout)

        print(f"✅ Threat Model Report Saved: {report_file}", flush=True)
    except Exception as e:
        print(f"❌ Error executing pytm: {e}", flush=True)

if __name__ == "__main__":
    run_pytm()
