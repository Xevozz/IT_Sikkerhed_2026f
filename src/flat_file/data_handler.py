import hashlib
from typing import Dict, Any, List, Optional

from src.flat_file.flat_file_loader import FlatFileLoader


REQUIRED_FIELDS = [
    "person_id",
    "first_name",
    "last_name",
    "address",
    "street_number",
    "password",
    "enabled",
]


class Data_Handler:
    def __init__(self, file_path: str):
        self.loader = FlatFileLoader(file_path)

    # ---------- Helping Methods ----------
    def _read_users(self) -> List[Dict[str, Any]]:
        data = self.loader.load()
        return data["users"]

    def _write_users(self, users: List[Dict[str, Any]]) -> None:
        self.loader.save({"users": users})

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    # ---------- public API ----------
    def get_number_of_users(self) -> int:
        return len(self._read_users())

    def create_user(
        self,
        person_id: int,
        first_name: str,
        last_name: str,
        address: str,
        street_number: int,
        password: str,
        enabled: bool = True,
    ) -> Dict[str, Any]:
        user = {
            "person_id": person_id,
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "street_number": street_number,
            "password": self._hash_password(password),
            "enabled": enabled,
        }

        # validate minimum
        for f in REQUIRED_FIELDS:
            if f not in user:
                raise ValueError(f"Missing field: {f}")

        users = self._read_users()

        if any(u["person_id"] == person_id for u in users):
            raise ValueError("person_id already exists")

        users.append(user)
        self._write_users(users)

        return user

    def get_user_by_id(self, person_id: int) -> Optional[Dict[str, Any]]:
        for u in self._read_users():
            if u["person_id"] == person_id:
                return u
        return None

    def disable_user(self, person_id: int) -> None:
        self._set_enabled(person_id, False)

    def enable_user(self, person_id: int) -> None:
        self._set_enabled(person_id, True)

    def _set_enabled(self, person_id: int, enabled: bool) -> None:
        users = self._read_users()
        for u in users:
            if u["person_id"] == person_id:
                u["enabled"] = enabled
                self._write_users(users)
                return
        raise ValueError("user not found")

    def authenticate(self, person_id: int, password: str) -> bool:
        u = self.get_user_by_id(person_id)
        if u is None:
            return False
        if u["enabled"] is not True:
            return False
        return u["password"] == self._hash_password(password)


# ----- Alias så tests kan import Data_handler -----

Data_handler = Data_Handler



