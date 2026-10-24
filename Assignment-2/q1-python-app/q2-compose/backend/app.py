from flask import Flask, jsonify
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import uuid

app = Flask(__name__)

REPORT_DIR = Path("/reports")


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/report")
def create_report():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    report = {
        "id": str(uuid.uuid4()),
        "message": "Report generated successfully",
        "generated_at": datetime.now(timezone.utc).isoformat()
    }

    filename = REPORT_DIR / f"{report['id']}.json"
    filename.write_text(json.dumps(report, indent=2), encoding="utf-8")

    return jsonify({
        "report": report,
        "saved_to": str(filename)
    })


@app.get("/reports")
def list_reports():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    reports = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(REPORT_DIR.glob("*.json"))
    ]

    return jsonify(reports)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
