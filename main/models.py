import re
from django.db import models


class BikerManager(models.Manager):

    def basic_validator(self, data):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        name = data['name']
        lastname = data['lastname']
        email = data['email']
        bike = data['bike']
        password = data['password']

        name_regex = re.compile(r'^[A-Z][a-z]+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(name) == 0:
            errors["name"] = "El nombre es requerido"
        elif name[0] == name[0].upper():
            errors["name"] = "El nombre debe comenzar por mayúsculas"
        elif not name_regex.match(name):
            errors["name"] = "El nombre debe comenzar con mayúsculas y tener después puras minusculas"
        
        if len(name) == 0:
            errors["lastname"] = "El apellido es requerido"
        elif name[0] == name[0].upper():
            errors["lastname"] = "El apellido debe comenzar por mayúsculas"
        elif not name_regex.match(name):
            errors["lastname"] = "El apellido debe comenzar con mayúsculas y tener después puras minúsculas"

        if not email_regex.match(email):    # probar si un campo coincide con el patrón        
            errors['email'] = "Dirección de email inválida"

        if bike not in ['urbana', 'treking', 'electrica', 'estatica']:
            errors['bike'] = "Debe seleccionar un tipo de bicicleta"
        
        if len(password) < 6:
            errors['password'] = "El largo de la contraseña debe ser  de al menos 6"
        elif password in ['password', '123456', '098765']:
            errors['password'] = "La contraseña no puede ser 'password', '123456' ni '098765'"

        return errors

class Biker(models.Model):

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    bike = models.CharField(max_length=255)

    objects = BikerManager()
