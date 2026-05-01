import json
from pathlib import Path

FILE = Path("data.json")

def load_data():
    if not FILE.exists():
        return []
    try:
        return json.loads(FILE.read_text())
    except json.JSONDecodeError:
        return []

def save_data(data):
    FILE.write_text(json.dumps(data, indent=2))