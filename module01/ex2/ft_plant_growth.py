class Plant:
    name_atr: str
    height_atr: float
    age_atr: int

    def info(self, n: str, h: float, a: int) -> None:
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


print("=== Garden Plant Growth ===")

flo = Plant()
flo.info("Lotus", 20.0, 5)
flo.show()
start = flo.height_atr

for i in range(1, 8):
    print(f"=== Day {i} ===")
    flo.grow()
    flo.age()
    flo.show()
print(f"Growth this week: {round(flo.height_atr - start, 1)}cm")
