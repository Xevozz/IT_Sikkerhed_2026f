import json
from pathlib import Path

class FlatFileUserDB:
    def __init__(self, path: Path):
        self.path = path
        if not self.path.exists():
            self.path.write_text("[]")

    def _load(self):
        return json.loads(self.path.read_text())

    def _save(self, data):
        self.path.write_text(json.dumps(data, indent=2))

    def create_user(self, user: dict):
        data = self._load()
        data.append(user)
        self._save(data)

    def get_user_by_id(self, person_id):
        return next((u for u in self._load() if u["person_id"] == person_id), None)
