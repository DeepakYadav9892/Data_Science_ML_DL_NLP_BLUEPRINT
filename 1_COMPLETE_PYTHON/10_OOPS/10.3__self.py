class Chaicup:
    size=150 

    def describe(self):
        return f"A {self.size}"

cup=Chaicup()
print(cup.describe())
print(Chaicup.describe())
cup_two=Chaicup()
cup_two.size=100
print(Chaicup.describe(cup_two))
print(cup_two.describe())
