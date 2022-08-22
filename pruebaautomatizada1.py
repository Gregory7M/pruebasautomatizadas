import unittest
import pymongo

'''def querydatos () :
    ''''''Crear un array para poder verificar si existen estos datos en mongodb ''''''
    coleccionTotal = coleccion.find ()
    usuarios =[]
    for busqueda in coleccionTotal :
        usuarios.append ( busqueda ['nombre','apellido','correo'])
    return usuarios'''


class Usuarios:
    '''
    Clase Usuarios.
    -----------
    Parametros
    -----------
        nombre: str
            ventana destinada a interfaces
        apellido: str
            Apellido del Usuario
        correo: str
            correo del Usuario
    ----------        
    Metodo
    ----------
        def __init__(self, nombre,apellido,correo):
            Constructor de la clase
    '''

    def __init__(self,nombre,apellido,correo):
            '''
            Construye todos los atributos necesarios para el Usuario.
            -----------
            Parametros
            -----------
            nombre: str
                Nombre del Usuario
            apellido: str
                Apellido del Usuario
            correo: str
                correo del Usuario
            '''
            self.nombre=nombre
            self.apellido=apellido
            self.correo=correo

    '''def validar(self):
        """PASAMOS EL DATO QUE SE ENCUENTRA EN LAS CAJAS DE TEXTO COMO PARAMETRO DE CADA ELEMENTO DE LA COLECCION"""
        self.coleccion.insert_one({"nombres":self.nombre.get(),"apellidos":self.apellido.get(),
        "correo":self.correo.get()})'''

class TestPython(unittest.TestCase):

    def test_invalid_dato1(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Karlos Gregory '
        apellido = 'Chevez Bazan'
        correo= 'gregorych99@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)

    def test_invalid_dato2(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Melany Domenica'
        apellido = 'Espinoza Vargas'
        correo= 'dome08@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)

    def test_invalid_dato3(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Karla'
        apellido = 'Paredes'
        correo= 'karlapa@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)
    
    def test_invalid_dato4(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Keila bela'
        apellido = 'Astudillo Acosta'
        correo= 'kbelen@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)

    def test_invalid_dato5(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Xavi '
        apellido = 'Chevez'
        correo= 'xavichevez@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)

    def test_invalid_dato6(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Andrea '
        apellido = 'Zambrano'
        correo= 'andrea09@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)

    def test_invalid_dato7(self):
        """
        Testea el ValueError de los datos ingresados
        """
        nombre = 'Cribel Anahis'
        apellido = 'Sisalima'
        correo= 'crissisa@gmial.com'
        with self.assertRaises(result):
            result = Usuarios(nombre,apellido,correo)        

if __name__ == '__main__':
    unittest.main()
        