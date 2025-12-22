class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milklevel = milk_level

    def sip(self):
        print("Sipping chai")

    def add_sugar(self, amount):
        print("added the sugar")


ravikant_chai = Chai(sweetness = 3, milk_level=2)
ravikant_chai.add_sugar(3)