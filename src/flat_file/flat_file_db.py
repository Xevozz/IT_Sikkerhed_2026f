import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.flat_file.flat_file_cryptography import Encryptor, PasswordHasher

SENSITIVE_FIELDS = {"first_name", "last_name", "adress", "street_number", "email", "telefon", "by"}


class FlatFileUserDB:
    def __init__(self, path: Path, encryptor: Encryptor, hasher: PasswordHasher):
        self.path = path
        self.encryptor = encryptor
        self.hasher = hasher

        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def _load(self) -> List[Dict[str, Any]]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data: List[Dict[str, Any]]) -> None:
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _encrypt_user_for_storage(self, user: Dict[str, Any]) -> Dict[str, Any]:
        u = dict(user)

        # Hash password (one-way) - aldrig kryptere password
        if "password" in u and u["password"] is not None:
            u["password"] = self.hasher.hash_password(u["password"])

        # Encrypt sensitive fields
        for field in SENSITIVE_FIELDS:
            if field in u and u[field] is not None:
                u[field] = self.encryptor.encrypt_str(str(u[field]))

        return u

    def _decrypt_user_for_use(self, user: Dict[str, Any]) -> Dict[str, Any]:
        u = dict(user)

        # Aldrig decrypt password (it's hashed)
        for field in SENSITIVE_FIELDS:
            if field in u and u[field] is not None:
                u[field] = self.encryptor.decrypt_str(u[field])

        return u

    def create_user(self, user: Dict[str, Any]) -> None:
        data = self._load()

        # unik person_id check
        pid = user.get("person_id")
        if any(x.get("person_id") == pid for x in data):
            raise ValueError("person_id already exists")

        encrypted = self._encrypt_user_for_storage(user)
        data.append(encrypted)
        self._save(data)

    def get_user_by_id(self, person_id: int, decrypt: bool = True) -> Optional[Dict[str, Any]]:
        data = self._load()
        user = next((u for u in data if u.get("person_id") == person_id), None)
        if not user:
            return None
        return self._decrypt_user_for_use(user) if decrypt else dict(user)

    def login(self, person_id: int, password: str) -> bool:
        """
        Decision table:
        - user findes?
        - enabled True?
        - password matcher hash?
        """
        data = self._load()
        user = next((u for u in data if u.get("person_id") == person_id), None)
        if not user:
            return False

        if user.get("enabled") is False:
            return False

        stored_hash = user.get("password", "")
        return self.hasher.verify_password(password, stored_hash)
