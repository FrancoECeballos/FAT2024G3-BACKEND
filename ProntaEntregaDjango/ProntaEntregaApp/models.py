# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class DireccionManager(models.Manager):
    def create_direccion(self, calle, numero, localidad):
        if not calle:
            raise ValueError('La dirección debe tener una calle')
        if not numero:
            raise ValueError('La dirección debe tener un número')
        if not localidad:
            raise ValueError('La dirección debe tener una localidad')

        direccion = self.model(
            calle=calle,
            numero=numero,
            localidad=localidad
        )
        direccion.save(using=self._db)
        return direccion
    
class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=255, blank=True, null=True)

    objects = DireccionManager()

    class Meta:
        managed = False
        db_table = 'Direccion'

    def __str__(self):
        return f"{self.calle} {self.numero}"


class Organizacion(models.Model):
    id_organizacion = models.AutoField(db_column='id_Organizacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organizacion'

    def __str__(self):
        return self.nombre


class Tipodocumento(models.Model):
    id_tipodocumento = models.AutoField(db_column='id_tipoDocumento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoDocumento'

    def __str__(self):
        return self.nombre


class Tipousuario(models.Model):
    id_tipousuario = models.AutoField(db_column='id_tipoUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoUsuario'

    def __str__(self):
        return self.nombre


class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, apellido, nombreusuario, documento, telefono, email, genero, imagen, id_direccion, id_tipousuario, id_tipodocumento, password):
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not apellido:
            raise ValueError('El usuario debe tener un apellido')
        if not nombreusuario:
            raise ValueError('El usuario debe tener un nombre de usuario')
        if not password:
            raise ValueError('El usuario debe tener una contraseña')
        if not documento:
            raise ValueError('El usuario debe tener un documento')

        usuario = self.model(
            nombre=nombre,
            apellido=apellido,
            nombreusuario=nombreusuario,
            documento=documento,
            telefono=telefono,
            email=self.normalize_email(email),
            genero=genero,
            imagen=imagen,
            id_direccion=id_direccion,
            id_tipousuario=id_tipousuario,
            id_tipodocumento=id_tipodocumento
        )
        usuario.set_password(password)  # Utiliza set_password para encriptar y guardar la contraseña
        usuario.is_active = True
        usuario.save(using=self._db)
        return usuario
    def create_superuser(self, nombre, apellido, password, nombreusuario, documento):
        usuario = self.model(
            nombre=nombre, 
            apellido=apellido, 
            nombreusuario=nombreusuario, 
            documento=documento, 
            telefono=None, 
            email=None, 
            id_direccion=None, 
            id_tipousuario=None, 
            id_tipodocumento=None)
        usuario.set_password(password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.is_active = True
        usuario.save(using=self._db)
        return usuario


class CustomUsuario(AbstractBaseUser, PermissionsMixin):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_UNKOWN = 3
    GENDER_CHOICES = [(GENDER_MALE, 'Hombre'), (GENDER_FEMALE, 'Mujer'), (GENDER_UNKOWN, 'Prefiero no decirlo')]

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=255, blank=True, null=True, unique=True)  # Field name made lowercase.
    documento = models.CharField(max_length=20, blank=True, null=True, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    genero = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    imagen = models.ImageField(upload_to='profilePictures/', null=True, blank=True)
    fechaUnion = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now, verbose_name='last login')
    id_direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, db_column='id_direccion', blank=True, null=True)
    id_tipousuario = models.ForeignKey(Tipousuario, on_delete=models.SET_NULL, db_column='id_tipoUsuario', blank=True, null=True)  # Field name made lowercase.
    id_tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.SET_NULL, db_column='id_tipoDocumento', blank=True, null=True)  # Field name made lowercase.
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'nombreusuario'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'documento']
    objects = UsuarioManager()

    class Meta:
        db_table = 'CustomUsuario'
        managed = False

    def __str__(self):
        return self.nombreusuario


class ObraManager(models.Manager):
    def create_obra(self, nombre, descripcion, id_organizacion, id_direccion):
        if not nombre:
            raise ValueError('La obra debe tener un nombre')
        if not descripcion:
            raise ValueError('La obra debe tener una descripción')
        if not id_organizacion:
            raise ValueError('La obra debe tener una organización')
        if not id_direccion:
            raise ValueError('La obra debe tener una dirección')
        

        Obra = self.model(
            nombre=nombre,
            descripcion=descripcion,
            id_organizacion=id_organizacion,
            id_direccion=id_direccion,
        )
        Obra.save(using=self._db)
        return Obra
    

class Obra(models.Model):
    id_obra = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_organizacion = models.ForeignKey('Organizacion', on_delete=models.SET_NULL, db_column='id_Organizacion', blank=True, null=True)  # Field name made lowercase.
    id_direccion = models.ForeignKey('Direccion', on_delete=models.SET_NULL, db_column='id_direccion', blank=True, null=True)
    imagen = models.ImageField(upload_to='obras/')

    objects = ObraManager()

    class Meta:
        db_table = 'Obra'
        managed = False


    def __str__(self):
        return self.nombre

class Detalleobrapedido(models.Model):
    id_detalleobrapedido = models.AutoField(db_column='id_DetalleObraPedido', primary_key=True)  # Field name made lowercase.
    id_obra = models.ForeignKey('Obra', models.DO_NOTHING, db_column='id_obra', blank=True, null=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleObraPedido'

class Detalleobrausuario(models.Model):
    id_detalleobrausuario = models.AutoField(db_column='id_detalleObraUsuario', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    id_obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, db_column='id_obra', blank=True, null=True)
    id_usuario = models.ForeignKey('CustomUsuario', on_delete=models.SET_NULL, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleObraUsuario'

    def __str__(self):
        return f'{self.id_detalleobrausuario}'

class Unidadmedida(models.Model):
    id_unidadmedida = models.AutoField(db_column='id_unidadMedida', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    identificador = models.CharField(max_length=20, blank=True, null=True)
    paquete = models.BooleanField(blank=True, default=False)

    class Meta:
        managed = False
        db_table = 'UnidadMedida'

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, db_column='id_obra', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stock'

    def __str__(self):
        return f'{self.id_obra}, Stock N°{self.id_stock}'
    

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='id_categoria', primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Categoria'

    def __str__(self):
        return self.nombre
    

class Categoriaproducto(models.Model):
    id_categoriaproducto = models.AutoField(db_column='id_categoriaProducto', primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CategoriaProducto'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_categoriaproducto = models.ForeignKey(Categoriaproducto, on_delete=models.SET_NULL, db_column='id_categoriaProducto', blank=True, null=True)
    id_unidadmedida = models.ForeignKey(Unidadmedida, on_delete=models.SET_NULL, db_column='id_unidadMedida', blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/')

    class Meta:
        managed = False
        db_table = 'Producto'

    def __str__(self):
        return str(self.id_producto)


class Detallestockproducto(models.Model):
    id_detallestockproducto = models.AutoField(db_column='id_detalleStockProducto', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    cantidadUnidades = models.IntegerField(default=1)
    id_stock = models.ForeignKey('Stock', on_delete=models.SET_NULL, db_column='id_stock', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, db_column='id_producto', blank=True, null=True)
    id_unidadmedida = models.ForeignKey('Unidadmedida', on_delete=models.SET_NULL, db_column='id_unidadMedida', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleStockProducto'

    def __str__(self):
        return f'{self.id_producto}, {self.id_stock}'


class Pedido(models.Model):
    urgencia_choices = [(1,'No es urgente'),(2,'Ligeramente urgente'),(3,'muy urgente'),(4,'inmediato')]

    id_pedido = models.AutoField(primary_key=True)  
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    horavencimiento = models.TimeField(db_column='horaVencimiento', blank=True, null=True)  # Field name made lowercase.
    id_obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, db_column='id_obra', blank=True, null=True)
    id_usuario = models.ForeignKey('CustomUsuario', on_delete=models.SET_NULL, db_column='id_usuario', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    urgente = models.IntegerField(choices=urgencia_choices,blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_estadoPedido = models.ForeignKey('Estadopedido', models.DO_NOTHING, db_column='id_estadoPedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pedido'

    def __str__(self):
        return str(self.id_pedido)


class Estadopedido(models.Model):
    id_estadopedido = models.AutoField(db_column='id_estadoPedido', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoPedido'

    def __str__(self):
        return self.nombre


class AportePedido(models.Model):
    id_aportePedido = models.AutoField(db_column='id_aportePedido', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AportePedido'


class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    horavencimiento = models.TimeField(db_column='horaVencimiento', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('CustomUsuario', on_delete=models.SET_NULL, db_column='id_usuario', blank=True, null=True)
    id_obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, db_column='id_obra', blank=True, null=True)
    id_estadooferta = models.ForeignKey('Estadooferta', on_delete=models.SET_NULL, db_column='id_estadoOferta', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Oferta'

    def __str__(self):
        return str(self.id_oferta)


class Estadooferta(models.Model):
    id_estadooferta = models.AutoField(db_column='id_estadoOferta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoOferta'

    def __str__(self):
        return self.nombre


class AporteOferta(models.Model):
    id_aporteOferta = models.AutoField(db_column='id_aporteOferta', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, db_column='id_oferta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AporteOferta'


class Transporte(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    patente = models.CharField(max_length=20, blank=True, null=True)
    kilometraje = models.IntegerField(blank=True, null=True)
    estadoitv = models.CharField(db_column='estadoITV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anio = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_organizacion = models.ForeignKey(Organizacion, on_delete=models.SET_NULL, db_column='id_Organizacion', blank=True, null=True)  # Field name made lowercase.
    imagen = models.ImageField(upload_to='vehiculos/')
    necesita_mantenimiento = models.BooleanField(default=False)
    descripcion_mantenimiento = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Transporte'

    def __str__(self):
        return str(self.id_transporte)

class CodigosDeVerificacion(models.Model):
    codigos_id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigos_de_verificacion'

class Notificacion(models.Model):
    notificacion_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    viewed = models.BooleanField(default=False)
    fecha_creacion = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey(CustomUsuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'

    def __str__(self):
        return str(self.notificacion_id)
