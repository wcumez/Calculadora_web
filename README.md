#  Calculadora Web 

Esta es una aplicación web desarrollada con Django,Python,HTML,CSS que permite calcular raíces de funciones matemáticas utilizando tres métodos numéricos:

- Método de Bisección
- Método de Newton-Raphson
- Método de Newton-Raphson Modificado

También muestra una tabla de iteraciones con los errores y una gráfica de la función ingresada.



## Características

- Interfaz web sencilla.
- Entrada de funciones simbólicas en términos de `x`.
- Soporte para visualizar gráficamente la función.
- Reporte detallado de las iteraciones con errores en porcentaje.



## Vista Principal

![App Screenshot](calculadora/img/v1.png)


## Vista Ventana de Resultados

![App Screenshot](calculadora/img/v1.png)






## 🧪 Métodos disponibles

1. **Bisección**  
   Método robusto que requiere un intervalo inicial `[a, b]` con cambio de signo.

2. **Newton-Raphson**  
   Método rápido que necesita una aproximación inicial `x0`.

3. **Newton-Raphson Modificado**  
   Variante del método de Newton que mejora la convergencia en polinomios con raíces múltiples.



## ⚙️ Requisitos

- Python 3.8 o superior
- Django 4.x
- SymPy
- Matplotlib
