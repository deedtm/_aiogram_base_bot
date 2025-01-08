import json
import os


dir_path = os.path.dirname(__file__)

with open(os.path.join(dir_path, 'templates.json')) as f:
    TEMPLATES: dict[str, str] = json.load(f)
    