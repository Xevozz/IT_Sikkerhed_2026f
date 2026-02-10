from dataclasses import dataclass, asdict

@dataclass
class User():
    person_id: int
    first_name: str
    last_name: str
    address: str
    street_number: int
    password: str
    enabled: bool = True

    def to_dict(self):
        return asdict(self)
    
    def from_dict(cls, data: "dict") -> "User":
        return User(**data)
