class DE():
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

    # y'(x) = 3y^(2/3)
    def get_prime(self, x, y):
        return 3 * (y ** (2/3))

    #С = 3 * y^(1/3) - 3 * x
    def get_constant(self):
        return 3 * ((self.y ** (1/3)) - self.x)

    #y(x) = (3 * x + C)^3 * 1/27
    def get_exact(self, x):
        return ((3 * x + self.get_constant()) ** 3) / 27
