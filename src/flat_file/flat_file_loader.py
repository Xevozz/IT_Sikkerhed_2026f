import json
import os
from typing import Dict, Any

class FlatFileLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.save({"users": []})

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return {"users": []}

        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return {"users": []}

        if not isinstance(data, dict) or "users" not in data or not isinstance(data["users"], list):
            return {"users": []}

        return data

    def save(self, data: Dict[str, Any]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
