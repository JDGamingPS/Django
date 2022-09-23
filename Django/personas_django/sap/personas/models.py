from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        #con el str muestra la persona en el navegador
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
#1.- hacemos la class modelo
#2.- ejecutamos el comando, python manage.py makemigrations <- para crear el archivo para la migracion pendiente que vamos a ejecutar
# para revisar el sql podemos usar el siguiente comando, python manage.py sqlmigrate personas 0001
# para crear la tabla en la base de datos ejecutamos, python manage.py migrate, que representa la classe