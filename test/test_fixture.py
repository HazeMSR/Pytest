"""
    Si se utiliza el parametro tempdir dentro
    de los parametros de la funcion de prueba,
    pytest buscara y llamara a una fábrica de
    'accesorios' o 'built-ins' para crear el
    recurso antes de realizar la llamada a la 
    función de la prueba. Antes de que se 
    ejecute la prueba, pytest crea un directorio 
    temporal de invocación único para la prueba.
"""
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
