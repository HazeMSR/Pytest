from src.functions import func


"""
    Esta es una prueba simple que importa la funcion func
    pasandole como parametro el numero 3 y 'asegura' que
    el valor de retorno sea 5. 
"""
def test_answer():
    assert func(3) == 3
""" Como el valor de retorno de func siempre va a ser 
    el parametro que recibe, esta prueba va a fallar.
""" 
