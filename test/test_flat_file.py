import pytest
from src.flat_file.data_handler import Data_handler

@pytest.fixture()
def db(tmp_path):
    return Data_handler(str(tmp_path / "users.json"))

def test_create_and_find_user(db):
    # GIVEN
    assert db.get_number_of_users() == 0

    # WHEN
    db.create_user(1, "John", "Doe", "Main Street", 10, "secret12")

    # THEN
    assert db.get_number_of_users() == 1
    user = db.get_user_by_id(1)
    assert user["first_name"] == "John"
    assert user["enabled"] is True
    assert user["password"] != "secret12"

def test_disable_enable_user(db):
    # GIVEN
    db.create_user(1, "A", "B", "X", 1, "secret12")
    db.create_user(2, "C", "D", "Y", 2, "secret22")

    # WHEN
    db.disable_user(1)

    # THEN
    assert db.get_user_by_id(1)["enabled"] is False
    assert db.get_user_by_id(2)["enabled"] is True

def test_authenticate_decision_table(db):
    # GIVEN
    db.create_user(1, "A", "B", "X", 1, "secret12")

    # R1
    assert db.authenticate(1, "secret12") is True
    # R2
    assert db.authenticate(1, "wrong") is False
    # R3
    db.disable_user(1)
    assert db.authenticate(1, "secret12") is False
    # R4
    assert db.authenticate(999, "secret12") is False
