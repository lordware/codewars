class Jar:
    def __init__(self):
        self.ml = 0
        self.jucies = {}

    def add(self, amount, kind):
        if kind in self.jucies:
            self.jucies[kind] += amount
        else:
            self.jucies[kind] = amount
        self.ml += amount

    def pour_out(self, amount):
        for key in self.jucies:
            new_amount = ((self.ml - amount) * self.jucies[key]) / self.ml
            self.jucies[key] = new_amount
        self.ml -= amount

    def get_total_amount(self):
        return self.ml

    def get_concentration(self, kind):
        if kind in self.jucies:
            return self.jucies[kind] / self.ml
        else:
            return 0
