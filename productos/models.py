from django.db import models


class Categoria (models.Model):
    id_categoria=models.AutoField(primary_key=True )
    tipo= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)

    def  __str__(self):
        return self.tipo
class Local (models.Model):
    adminLocal=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    categoria=models.ForeignKey('Categoria',on_delete=models.CASCADE)
    id_local=models.AutoField(primary_key=True )
    nombreComercial= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=180)
    srcLogo= models.ImageField(verbose_name="Imagen")
    direccion= models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    latitud= models.CharField(max_length=50)
    like=models.IntegerField()
    estrella=models.IntegerField()
    vistas=models.IntegerField()
    def  __str__(self):
        return self.nombreComercial
class Escaneos (models.Model):
    id_Escaneos=models.AutoField(primary_key=True )
    fecha=models.DateField(blank=True, null=True)
    lugar = models.CharField(max_length=55)
    celular=models.IntegerField()
    def  __str__(self):
        return self.id_Escaneos 
class Permiso (models.Model):
    id_Permiso=models.AutoField(primary_key=True )
    descripcion = models.CharField(max_length=180)
    tipo=models.CharField(max_length=20)
    
    def  __str__(self):
        return self.id_Permiso 
