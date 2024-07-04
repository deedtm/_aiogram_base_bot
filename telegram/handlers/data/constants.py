import json

with open(r'telegram\handlers\data\templates.json') as f:
    TEMPLATES: dict[str, str] = json.load(f)
    