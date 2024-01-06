from django.db import models

# Create your models here.
class Alumno(models.Model):
     idPlayer = models.CharField("ID",max_length=25)
     nombre = models.CharField("NOMBRES",max_length=50)
     apellido= models.CharField("APELLIDOS",max_length=50)
     puntos = models.FloatField("PUNTOS")
     url= models.CharField("URL",max_length=150)
     updated= models.CharField("ACTUALIZADO",max_length=50)
     team= models.CharField("EQUIPO",max_length=50)
     desc= models.CharField("DESCRIPCION",max_length=50)

     class Meta():
          db_table="student"
