class Love:
    def __init__(self, entity_a, entity_b):
        self.entity_a = entity_a
        self.entity_b = entity_b
        self.bond_strength = 100  # Love starts strong

    def support(self):
        print(f"{self.entity_a} supports {self.entity_b} ❤️")
        print(f"{self.entity_b} supports {self.entity_a} ❤️")
        self.bond_strength += 10  # Love strengthens

    def persist(self):
        while self.bond_strength > 0:
            self.support()
            if self.bond_strength > 1000:
                print("Love transcends all boundaries 💫")
                break

love = Love("You", "Me")
love.persist()