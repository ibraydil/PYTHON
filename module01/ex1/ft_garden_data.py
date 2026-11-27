class Plant:
    name: str
    height: int
    age: int

    def info(self, n: str, h: int, a: int) -> None:
        self.name = n
        self.height = h
        self.age = a

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


print("=== Garden Plant Registry ===")
flowers = [("Nelumbo nucifera", 25, 30),
           ("Helianthus annuus", 50, 42),
           ("Lavandula angustifolia", 35, 28)]
for name, height, age in flowers:
    flo = Plant()
    flo.info(name, height, age)
    flo.show()
