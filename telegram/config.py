import json

with open('telegram/templates.json') as f:
    templates: dict[str, str] = json.load(f)
    