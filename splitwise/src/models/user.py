class User:
    def __init__(self, id: str, name: str, email: str, phone: str) -> None:
        self.id: str = id
        self.name: str = name
        self.email: str = email
        self.phone: str = phone

    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str) -> None:
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email = email

    def get_phone(self) -> str:
        return self.phone

    def set_phone(self, phone: str) -> None:
        self.phone = phone