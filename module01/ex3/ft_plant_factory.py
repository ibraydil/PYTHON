class Plant:

    def __init__(self, n: str = "name",
                 h: float = 5.0,
                 a: int = 1) -> None:
        self.name_atr = n
        self.height_atr = h
        self.age_atr = a

    def show(self) -> None:
        print(f"{self.name_atr}: {self.height_atr}cm, {self.age_atr} days old")

    def grow(self, extra: float = 0.2) -> None:
        self.height_atr += extra
        self.height_atr = round(self.height_atr, 1)

    def age(self, day: int = 1) -> None:
        self.age_atr += day


print("=== Plant Factory Output ===")
flowers = [("Lotus", 20.0, 5),
           ("Sunflower", 30.0, 15),
           ("Lavender", 15.0, 8),
           ("Rose", 25.0, 30),
           ("Cactus", 7.0, 6)]

for name, height, age in flowers:
    flo = Plant(name, height, age)
    print("Created: ", end="")
    flo.show()
