import tkinter as tk
from equation import DE
from methods import *
import matplotlib.pyplot as plt


def get_info():
    info = tk.Tk()

    tk.Label(info, text="Get Info").grid(row=0)
    tk.Label(info, text="x_0").grid(row=1)
    tk.Label(info, text="y_0").grid(row=2)
    tk.Label(info, text="X").grid(row=3)
    tk.Label(info, text="Number of points").grid(row=4)
    tk.Label(info, text="total approximation error depending on the number of grid cells").grid(row=5)
    tk.Label(info, text="n_0").grid(row=6)
    tk.Label(info, text="N_max").grid(row=7)
    tk.Label(info, text="Equation = y'(x) = 3*y^(2/3)").grid(row=8)

    x0_field = tk.Entry(info)
    y0_field = tk.Entry(info)
    X_field = tk.Entry(info)
    N_field = tk.Entry(info)
    n_start_field = tk.Entry(info)
    n_finish_field = tk.Entry(info)

    x0_field.grid(row=1, column=1)
    y0_field.grid(row=2, column=1)
    X_field.grid(row=3, column=1)
    N_field.grid(row=4, column=1)
    n_start_field.grid(row=6, column=1)
    n_finish_field.grid(row=7, column=1)

    def create():
        x0 = float(x0_field.get())
        y0 = float(y0_field.get())
        X = float(X_field.get())
        N = int(N_field.get())
        n_start = int(n_start_field.get())
        n_finish = int(n_finish_field.get())

        equation = DE(x0, y0)

        x_Exact, y_Exact = Exact.build(equation, x0, X, N)
        x_Euler, y_Euler = Euler.build(equation, x0, X, N)
        x_ImpEuler, y_ImpEuler = ImprovedEuler.build(equation, x0, X, N)
        x_RK, y_RK = RungeKutta.build(equation, x0, X, N)

        L_Euler, L_ImpEuler, L_RK = Euler.get_lte(y_Exact, y_Euler), \
                                    ImprovedEuler.get_lte(y_Exact, y_ImpEuler), \
                                    RungeKutta.get_lte(y_Exact, y_RK)

        G_x = range(n_start, n_finish + 1)
        G_Euler, G_ImpEuler, G_RK = Euler.get_gte(equation, n_start, n_finish, x0, X), \
                                    ImprovedEuler.get_gte(equation, n_start, n_finish, x0, X), \
                                    RungeKutta.get_gte(equation, n_start, n_finish, x0, X)

        plt.subplot(2, 1, 1)
        plt.title('Solutions')
        plt.plot(x_Exact, y_Exact, label="Exact", color='yellow')
        plt.plot(x_Euler, y_Euler, label="Euler", color='blue')
        plt.plot(x_ImpEuler, y_ImpEuler, label="Improved Euler", color='red')
        plt.plot(x_RK, y_RK, label="Runge-Kutta", color='green')
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.title('LTE')
        plt.plot(x_Euler, L_Euler, label="Euler", color='blue')
        plt.plot(x_ImpEuler, L_ImpEuler, label="Improved Euler", color='red')
        plt.plot(x_RK, L_RK, label="Runge-Kutta", color='green')
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.title('GTE')
        plt.plot(G_x, G_Euler, label="Euler", color='blue')
        plt.plot(G_x, G_ImpEuler, label="Improved Euler", color='red')
        plt.plot(G_x, G_RK, label="Runge-Kutta", color='green')
        plt.legend()

        plt.show()

    button = tk.Button(None, text='Create', command=create)
    button.grid(row=9)

    info.mainloop()


get_info()
