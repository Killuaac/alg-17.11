class Bank:
    def __init__(self, inf, count, num_of_ops):
        self.inf = inf
        self.count = count
        self.num_of_ops = num_of_ops

    def get_user(self):
        return (f'{self.inf}: остаток по счету: {self.count}, '
                f'кол-во операций: {self.num_of_ops}')

    def get_inf(self, inf):
        return inf

    def get_count(self, count):
        return count

    def get_num_f_ops(self, num_of_ops):
        return num_of_ops

    def add_count(self, adding):
        self.num_of_ops += 1
        self.count += adding

    def reduce_count(self, reducing):
        self.num_of_ops += 1
        self.count -= reducing


b = Bank('Олежа - нищий', 500, 0)
b.add_count(100)
b.reduce_count(400)
print(b.get_user())
