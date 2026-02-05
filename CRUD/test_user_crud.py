import pytest

from CRUD.user_crud import (
    create_user, read_user, update_user, delete_user, list_users,
    NotFound, AlreadyExist, WeakPassword
)

def test_create_user_success():
    db = {}
    user = create_user(db, "niklas", "Strong123!")
    assert user["username"] == "niklas"
    assert db["niklas"]["password"] == "Strong123!"

def test_create_user_duplicate_raises():
    db = {}
    create_user(db, "niklas", "Strong123!")
    with pytest.raises(AlreadyExist):
        create_user(db, "niklas", "Strong123!")

def test_create_user_weak_password_raises():
    db = {}
    with pytest.raises(WeakPassword):
        create_user(db, "niklas", "weak")  # for kort + ingen tal + ingen specialtegn

def test_read_user_success():
    db = {}
    create_user(db, "niklas", "Strong123!")
    user = read_user(db, "niklas")
    assert user["username"] == "niklas"

def test_read_user_not_found_raises():
    db = {}
    with pytest.raises(NotFound):
        read_user(db, "ghost")

def test_update_user_success():
    db = {}
    create_user(db, "niklas", "Strong123!")
    updated = update_user(db, "niklas", "Newpass123#")
    assert updated["password"] == "Newpass123#"
    assert db["niklas"]["password"] == "Newpass123#"

def test_update_user_not_found_raises():
    db = {}
    with pytest.raises(NotFound):
        update_user(db, "ghost", "Strong123!")

def test_update_user_weak_password_raises():
    db = {}
    create_user(db, "niklas", "Strong123!")
    with pytest.raises(WeakPassword):
        update_user(db, "niklas", "short1!")  # 7 tegn -> for kort

def test_delete_user_success():
    db = {}
    create_user(db, "niklas", "Strong123!")
    delete_user(db, "niklas")
    assert "niklas" not in db

def test_delete_user_not_found_raises():
    db = {}
    with pytest.raises(NotFound):
        delete_user(db, "ghost")

def test_list_users_returns_all_users():
    db = {}
    create_user(db, "niklas", "Strong123!")
    create_user(db, "bob", "Strong456#")

    users = list_users(db)
    assert len(users) == 2
    assert any(u["username"] == "niklas" for u in users)
    assert any(u["username"] == "bob" for u in users)