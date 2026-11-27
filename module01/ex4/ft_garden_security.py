class Plant:

    def __init__(self, n: str = "name",
                 h: float = 5.0,
                 a: int = 1) -> None:
        self._name = n
        self._height = h
        self._age = a

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, extra: float = 0.2) -> None:
        self._height += extra
        self._height = round(self._height, 1)

    def age(self, day: int = 1) -> None:
        self._age += day


print("=== Garden Security System ===")
flo = Plant("Rose", 15.0, 10)
print("Plant created: ", end="")
flo.show()
flo.set_height(25.0)
flo.set_age(30)
flo.set_height(-5.0)
flo.set_age(-3)
print("Current state: ", end="")
flo.show()
