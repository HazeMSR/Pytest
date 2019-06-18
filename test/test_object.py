"""
    Se pueden agrupar distintas pruebas en una sola clase,
    deben contener en su nombre 'test_' de manera prefija,
    para que los detecte el compilador de pytest. La 
    primera prueba va a concluir de manera exitosa, sin 
    embargo, la segunda prueba terminara en error.
"""
class TestClass(object):
    
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = {"check": "heck"}
        assert hasattr(x, 'check')
