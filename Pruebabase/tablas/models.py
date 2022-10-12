from secrets import choice
from django.db import models

# Create your models here.
class Pais(models.Model):    
    pais = models.CharField(max_length=100,verbose_name='pais')
    nacionalidad = models.CharField(max_length=100,verbose_name='nacionalidad')
    ISOnac = models.CharField(max_length=100,verbose_name='ISOnac')
    def __str__(self):
        fila = 'Pais: ' + self.pais + ' Nacionalidad: ' + self.nacionalidad
        return fila

paises = Pais.objects.all()
choicepais = [(0,"")]
for pais in paises:
    choicepais.append((pais.id,pais.pais))


class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='id')
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    nacimiento = models.DateField(verbose_name='nacimiento')
    paisp = models.IntegerField(verbose_name='pais',choices = choicepais)
    nacionalidadp = models.CharField(max_length=100,verbose_name='nacionalidad')
    def __str__(self):
        fila = 'ID: ' + str(self.id) + ' Nombre: ' + self.nombre
        return fila
    def delete(self):
        super().delete()
    def strdt(self):
        strdatetime = self.nacimiento.strftime("%m-%d-%Y")
        return strdatetime
    def strpais(self):
        idpais = str(self.paisp)
        strpais = idpais
        for tupl in choicepais:
            if (idpais == str(tupl[0])):
                strpais = tupl[1]
        return strpais


