from sympy import sympify, Symbol, diff
import numpy as np

x = Symbol('x')

def evaluar(func, val):
    return float(sympify(func).subs(x, val))

def biseccion(funcion, a, b, tol, max_iter):
    tabla = []
    f = sympify(funcion)
    fa = evaluar(f, a)
    fb = evaluar(f, b)

    if fa * fb > 0:
        raise ValueError("No hay cambio de signo en el intervalo [a, b].")

    c_anterior = a  # Inicializar c_anterior para evitar división por cero

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = evaluar(f, c)

        # Calcular error en porcentaje (salta la primera iteración)
        if i == 1:
            error = 100 
        else:
            error = abs((c - c_anterior) / c) * 100

        tabla.append({'i': i, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'error (%)': error})

        if error is not None and error < tol or fc == 0:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_anterior = c

    return tabla, c


# Método de Newton-Raphson
def newton_raphson(funcion, x0, tol, max_iter):
    f = sympify(funcion)
    f_prime = diff(f, x)
    tabla = []
    x_anterior = x0

    for i in range(1, max_iter + 1):
        fx = evaluar(f, x_anterior)
        fpx = evaluar(f_prime, x_anterior)

        if fpx == 0:
            raise ZeroDivisionError("Derivada cero. Método no aplicable.")

        x1 = x_anterior - fx / fpx

        # Calcular error desde la segunda iteración
        if i == 1:
            error = 100
        else:
            error = abs((x1 - x_anterior) / x1) * 100 if x1 != 0 else 0

        tabla.append({
            'i': i,
            'x': x_anterior,
            'f(x)': fx,
            "f'(x)": fpx,
            'x1': x1,
            'error (%)': error
        })

        if error is not None and error < tol:
            break

        x_anterior = x1

    return tabla, x1


# Método de Newton-Raphson Modificado
def newton_raphson_modificado(funcion, x0, tol, max_iter):
    f = sympify(funcion)
    f_prime = diff(f, x)
    f_double_prime = diff(f_prime, x)
    tabla = []
    x_anterior = x0

    for i in range(1, max_iter + 1):
        fx = evaluar(f, x_anterior)
        fpx = evaluar(f_prime, x_anterior)
        fppx = evaluar(f_double_prime, x_anterior)

        denominador = fpx**2 - fx * fppx
        if denominador == 0:
            raise ZeroDivisionError("División por cero en fórmula modificada.")

        x1 = x_anterior - (fx * fpx) / denominador

        # Calcular error desde la segunda iteración
        if i == 1:
            error = 100
        else:
            error = abs((x1 - x_anterior) / x1) * 100 if x1 != 0 else 0

        tabla.append({
            'i': i,
            'x': x_anterior,
            'f(x)': fx,
            "f'(x)": fpx,
            "f''(x)": fppx,
            'x1': x1,
            'error (%)': error
        })

        if error is not None and error < tol:
            break

        x_anterior = x1

    return tabla, x1
