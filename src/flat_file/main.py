from src.flat_file.data_handler import Data_handler

if __name__ == "__main__":
    db = Data_handler("users.json")
    db.create_user(1, "John", "Doe", "Main Street", 10, "secret12")
    print(db.authenticate(1, "secret12"))  # True
