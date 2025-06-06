import re

def limpiar_funcion(funcion_usuario):
    # Reemplaza ^ por **
    funcion_limpia = funcion_usuario.replace('^', '**')

    # Inserta * entre número y variable: 2x → 2*x
    funcion_limpia = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion_limpia)

    # Inserta * entre variables si hay más de una letra seguida (por ejemplo: xx)
    funcion_limpia = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', funcion_limpia)

    return funcion_limpia
