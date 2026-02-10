import os
import base64
import hashlib
import hmac
import secrets
from dataclasses import dataclass
from cryptography.fernet import Fernet



# Encryption (Fernet)
@dataclass
class Encryptor:
    fernet: Fernet

    @staticmethod
    def from_env(var_name: str = "FLATFILE_DB_KEY") -> "Encryptor":
        key = os.getenv(var_name)
        if not key:
            raise RuntimeError(
                f"Mangler env var '{var_name}'. Sæt den til en Fernet key. "
                f"Generér med: python3 -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\""
            )
        return Encryptor(Fernet(key.encode("utf-8")))

    def encrypt_str(self, value: str) -> str:
        if value is None:
            return value
        token = self.fernet.encrypt(value.encode("utf-8"))
        return token.decode("utf-8")

    def decrypt_str(self, token: str) -> str:
        if token is None:
            return token
        value = self.fernet.decrypt(token.encode("utf-8"))
        return value.decode("utf-8")



# Password hashing (PBKDF2)
@dataclass
class PasswordHasher:
    iterations: int = 210_000 #nøglestrækningsfaktor

    def hash_password(self, password: str) -> str:
        if not isinstance(password, str) or len(password) == 0:
            raise ValueError("Kodeord skal være en ikke-tom streng.")

        salt = secrets.token_bytes(16)
        dk = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            self.iterations,
            dklen=32,
        )

        salt_b64 = base64.urlsafe_b64encode(salt).decode("utf-8")
        dk_b64 = base64.urlsafe_b64encode(dk).decode("utf-8")
        return f"pbkdf2${self.iterations}${salt_b64}${dk_b64}"

    def verify_password(self, password: str, stored: str) -> bool:
        try:
            algo, it_s, salt_b64, dk_b64 = stored.split("$", 3)
            if algo != "pbkdf2":
                return False

            iterations = int(it_s)
            salt = base64.urlsafe_b64decode(salt_b64.encode("utf-8"))
            dk_expected = base64.urlsafe_b64decode(dk_b64.encode("utf-8"))
        except Exception:
            return False

        dk = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations,
            dklen=len(dk_expected),
        )
        return hmac.compare_digest(dk, dk_expected)

        