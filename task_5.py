class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def type(self, a, b, c):
        if a == b and a == c:
            return 'равносторонний'
        elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a) or (c == a and c != b):
            return 'равнобедренный'
        elif a != b and a != c and b != c:
            return 'разносторонный'
