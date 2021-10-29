class Exact:
    @staticmethod
    def calculate_point(equation, x, y, step):
        return equation.get_exact(x)

    @staticmethod
    def build(equation, x, x_end, N):
        step = (x_end - x) / (N - 1)
        X, Y = [x], [equation.get_exact(x)]

        for i in range(1, N):
            X.append(X[i - 1] + step)
            Y.append(equation.get_exact(X[i]))

        return X, Y


class Euler:
    @staticmethod
    def calculate_point(equation, x, y, step):
        return y + equation.get_prime(x, y) * step

    @staticmethod
    def build(equation, x, x_end, N):
        step = (x_end - x) / (N - 1)
        X, Y = [x], [equation.get_exact(x)]

        for i in range(1, N):
            X.append(X[i - 1] + step)
            Y.append(Euler.calculate_point(equation, X[i - 1], Y[i - 1], step))

        return X, Y

    @staticmethod
    def get_lte(y_exact, y_method):
        LTE = []

        for i in range(0, len(y_exact)):
            LTE.append(abs(y_exact[i] - y_method[i]))

        return LTE

    @staticmethod
    def get_gte(equation, n_start, n_finish, x, x_end):
        GTE = []

        for i in range(n_start, n_finish + 1):
            GTE.append(max(Euler.get_lte(Exact.build(equation, x, x_end, i)[1], Euler.build(equation, x, x_end, i)[1])))

        return GTE


class ImprovedEuler:
    @staticmethod
    def calculate_point(equation, x, y, step):
        return y + equation.get_prime(x + step / 2, y + (step / 2) * equation.get_prime(x, y)) * step

    @staticmethod
    def build(equation, x, x_end, N):
        step = (x_end - x) / (N - 1)
        X, Y = [x], [equation.get_exact(x)]

        for i in range(1, N):
            X.append(X[i - 1] + step)
            Y.append(ImprovedEuler.calculate_point(equation, X[i - 1], Y[i - 1], step))

        return X, Y

    @staticmethod
    def get_lte(y_exact, y_method):
        LTE = []

        for i in range(0, len(y_exact)):
            LTE.append(abs(y_exact[i] - y_method[i]))

        return LTE

    @staticmethod
    def get_gte(equation, n_start, n_finish, x, x_end):
        GTE = []

        for i in range(n_start, n_finish + 1):
            GTE.append(max(ImprovedEuler.get_lte(Exact.build(equation, x, x_end, i)[1],
                                                 ImprovedEuler.build(equation, x, x_end, i)[1])))

        return GTE


class RungeKutta:
    @staticmethod
    def calculate_point(equation, x, y, step):
        k1 = equation.get_prime(x, y)
        k2 = equation.get_prime(x + step / 2, y + step * k1 / 2)
        k3 = equation.get_prime(x + step / 2, y + step * k2 / 2)
        k4 = equation.get_prime(x + step, y + step * k3)

        return y + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    @staticmethod
    def build(equation, x, x_end, N):
        step = (x_end - x) / (N - 1)
        X, Y = [x], [equation.get_exact(x)]

        for i in range(1, N):
            X.append(X[i - 1] + step)
            Y.append(RungeKutta.calculate_point(equation, X[i - 1], Y[i - 1], step))

        return X, Y

    @staticmethod
    def get_lte(y_exact, y_method):
        LTE = []

        for i in range(0, len(y_exact)):
            LTE.append(abs(y_exact[i] - y_method[i]))

        return LTE

    @staticmethod
    def get_gte(equation, n_start, n_finish, x, x_end):
        GTE = []

        for i in range(n_start, n_finish + 1):
            GTE.append(max(
                RungeKutta.get_lte(Exact.build(equation, x, x_end, i)[1], RungeKutta.build(equation, x, x_end, i)[1])))

        return GTE
