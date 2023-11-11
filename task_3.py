class Car:
    def __init__(self, mark, model, year, mileage):
        self.mark = mark
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage


c = Car('Toyota', 'mark 2', '1999', '100000')
c.set_mark('Nissan')
print(c.get_mark())