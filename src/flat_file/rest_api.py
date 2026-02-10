from src.flat_file.data_handler import Data_handler

def login(db_path: str, person_id: int, password: str) -> bool:
    db = Data_handler(db_path)
    return db.authenticate(person_id, password)
