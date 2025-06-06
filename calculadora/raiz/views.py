import matplotlib.pyplot as plt
import numpy as np
import os
import uuid
from django.conf import settings
from django.shortcuts import render
from .forms import MetodoForm
from .metodos import biseccion, newton_raphson, newton_raphson_modificado  # importa todos

def resultado(request):
    if request.method == 'POST':
        form = MetodoForm(request.POST)
        if form.is_valid():
            fx = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            tol = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']

            try:
                from sympy import sympify, lambdify, Symbol
                x = Symbol('x')
                f_expr = sympify(fx)
                f_lamb = lambdify(x, f_expr, 'numpy')

                if metodo == 'biseccion':
                    a = form.cleaned_data['a']
                    b = form.cleaned_data['b']
                    tabla, raiz = biseccion(fx, a, b, tol, max_iter)
                    x_vals = np.linspace(a, b, 400)

                elif metodo == 'newton':
                    x0 = form.cleaned_data['a']
                    tabla, raiz = newton_raphson(fx, x0, tol, max_iter)
                    x_vals = np.linspace(x0 - 5, x0 + 5, 400)

                elif metodo == 'newton_mod':
                    x0 = form.cleaned_data['a']
                    tabla, raiz = newton_raphson_modificado(fx, x0, tol, max_iter)
                    x_vals = np.linspace(x0 - 5, x0 + 5, 400)

                # Generar gráfica
                y_vals = f_lamb(x_vals)
                plt.figure(figsize=(6, 4))
                plt.plot(x_vals, y_vals, label=f'f(x) = {fx}')
                plt.axhline(0, color='gray', linestyle='--')
                plt.axvline(raiz, color='red', linestyle='--', label='Raíz aprox.')
                plt.title('Gráfica del polinomio')
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.grid(True)
                plt.legend()

                nombre_archivo = f"{uuid.uuid4()}.png"
                ruta_absoluta = os.path.join(settings.MEDIA_ROOT, nombre_archivo)
                plt.savefig(ruta_absoluta)
                plt.close()

                return render(request, 'raiz/resultado.html', {
                'tabla': tabla,
                'raiz': raiz,
                'funcion': fx,
                'grafica_url': settings.MEDIA_URL + nombre_archivo,
                'metodo': metodo,  # ✅ Esto es lo que debes agregar
})


            except Exception as e:
                return render(request, 'raiz/resultado.html', {'error': str(e)})
    else:
        form = MetodoForm()
    return render(request, 'raiz/index.html', {'form': form})


def index(request):
    form = MetodoForm()
    return render(request, 'raiz/index.html', {'form': form})
