from django import forms

class MetodoForm(forms.Form):
    METODOS = [
        ('biseccion', 'Bisección'),
        ('newton', 'Newton-Raphson'),
        ('newton_mod', 'Newton-Raphson Modificado'),
    ]

    funcion = forms.CharField(label='f(x)', max_length=100)
    metodo = forms.ChoiceField(choices=METODOS)
    a = forms.FloatField(label='a / x0')  # sirve como intervalo o punto inicial
    b = forms.FloatField(required=False, label='b')  # solo se usa para bisección
    tolerancia = forms.FloatField(label='Tolerancia (%)')
    max_iter = forms.IntegerField(label='Máx Iteraciones')
