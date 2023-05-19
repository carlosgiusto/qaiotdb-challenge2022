#Uso 'unittest' para realizar las verificaciones en los casos de prueba
import unittest
from get_character_info import get_character_info

class TestGetCharacterInfo(unittest.TestCase):

    def test_existing_character(self):
        info = get_character_info("rick")
        self.assertIsInstance(info, list)  # Verificando que el resultado es una lista
        self.assertGreater(len(info), 0)   # Verificando que la lista no esté vacía

    def test_nonexistent_character(self):
        info = get_character_info("PersonajeQueNoExiste")
        self.assertEqual(info, "El personaje no fue encontrado.")  # Verificando que el resultado es el string correcto cuando un personaje no existe

    def test_empty_character_name(self):
        info = get_character_info("")
        self.assertEqual(info, "El nombre del personaje no puede estar vacío.")  # Verificando que el resultado es el string correcto cuando el campo de busqueda esta vacio

    def test_special_character_in_name(self):
        info = get_character_info("rick&morty")
        self.assertIn(info, "El nombre del personaje no puede contener caracteres especiales.")  # Verificando que el resultado sea el string correcto cuando el campo de busqueda un caracter especial
        


if __name__ == '__main__':
    unittest.main()