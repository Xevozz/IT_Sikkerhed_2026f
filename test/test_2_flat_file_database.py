from src.flat_file.flat_file_db import FlatFileUserDB

def test_create_user_is_saved(tmp_path):
    # Given
    db = FlatFileUserDB(tmp_path / "users.json")
    user = {
        "person_id": 1,
        "first_name": "Niklas",
        "last_name": "Pedersen",
        "adress": "Testvej",
        "street_number": "1",
        "password": "Secret123",
        "enabled": True
    }

    # When
    db.create_user(user)

    # Then
    loaded = db.get_user_by_id(1)
    assert loaded["person_id"] == 1
