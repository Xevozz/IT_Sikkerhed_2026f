def test_show_json_file_and_verify_encryption(tmp_path, monkeypatch):
    from cryptography.fernet import Fernet
    from src.flat_file.flat_file_db import FlatFileUserDB
    from src.flat_file.flat_file_cryptography import Encryptor, PasswordHasher

    # Given
    monkeypatch.setenv("FLATFILE_DB_KEY", Fernet.generate_key().decode())

    json_path = tmp_path / "users.json"
    db = FlatFileUserDB(
        json_path,
        Encryptor.from_env("FLATFILE_DB_KEY"),
        PasswordHasher()
    )

    user = {
        "person_id": 1,
        "first_name": "Niklas",
        "last_name": "Pedersen",
        "adress": "Testvej",
        "street_number": "1",
        "email": "n@test.dk",
        "telefon": "12345678",
        "by": "Roskilde",
        "password": "Secret123",
        "enabled": True,
    }

    # When
    db.create_user(user)

    # Then – PRINT BEVIS
    print("\n================ JSON FILE INSPECTION ================")
    print("JSON path:", json_path)
    print("JSON content:\n", json_path.read_text(encoding="utf-8"))
    print("=====================================================\n")

    raw = json_path.read_text(encoding="utf-8")

    # Assertions (automatisk bevis)
    assert "Niklas" not in raw
    assert "Pedersen" not in raw
    assert "n@test.dk" not in raw
    assert "Secret123" not in raw
    assert "pbkdf2$" in raw

