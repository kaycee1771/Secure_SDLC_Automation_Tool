import sys
import os
from jinja2 import Template
from pytm.pytm import TM, Server, Dataflow, Datastore, Boundary

def define_threat_model():
    """Defines a threat model explicitly for pytm."""
    tm = TM("Secure SDLC Threat Model")
    tm.description = "Automatically generated threat model."

    # Define boundaries
    boundary_external = Boundary("External")
    boundary_internal = Boundary("Internal")

    # Define components
    web_server = Server("Web Server")
    web_server.boundary = boundary_internal

    database = Datastore("Database")
    database.boundary = boundary_internal

    external_user = Server("External User")
    external_user.boundary = boundary_external

    # Define data flows
    Dataflow(external_user, web_server, "User sends request")
    Dataflow(web_server, database, "Web server queries database")

    return tm

if __name__ == "__main__":
    sys.argv = [sys.argv[0]]  # Prevent argparse conflicts

    # Define the template file path
    template_path = "C:/Users/kaytn/secure_sdlc_automation/src/threat_modeling/report_template.txt"

    # Ensure the template file exists
    if not os.path.exists(template_path):
        with open(template_path, "w", encoding="utf-8") as template_file:
            template_file.write(
                "Threat Model: {{ tm.name }}\n"
                "=================================\n"
                "Description: {{ tm.description }}\n\n"
                "Entities:\n"
                "{% for e in tm._elements %}\n"
                "  - {{ e.name }} (Type: {{ e.__class__.__name__ }})\n"
                "{% endfor %}\n\n"
                "Data Flows:\n"
                "{% for df in tm._dataflows %}\n"
                "  - {{ df.name }} ({{ df.source.name }} → {{ df.sink.name }})\n"
                "{% endfor %}\n\n"
                "Threats Identified:\n"
                "{% for t in tm._threats %}\n"
                "  - {{ t.name }} | Severity: {{ t.severity }} | Category: {{ t.category | default('Uncategorized') }} | Description: {{ t.description }}\n"
                "{% endfor %}\n"
            )

    # Process the threat model
    tm = define_threat_model()
    tm.process()

    # Load and render the template using Jinja2
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    jinja_template = Template(template_content)
    report_content = jinja_template.render(tm=tm)

    # Save to file
    report_file = "C:/Users/kaytn/secure_sdlc_automation/reports/threat_model_report.txt"
    with open(report_file, "w", encoding="utf-8") as file:
        file.write(report_content)

    print(f"✅ Threat Model Report Saved: {report_file}")
