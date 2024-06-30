class ExpenseMetadata:
    def __init__(self, name: str, img_url: str, notes: str) -> None:
        self.name: str = name
        self.img_url: str = img_url
        self.notes: str = notes

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_img_url(self) -> str:
        return self.img_url

    def set_img_url(self, img_url: str) -> None:
        self.img_url = img_url

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes