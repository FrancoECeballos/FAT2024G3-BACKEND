# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Casa(models.Model):
    id_casa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_organizacion = models.ForeignKey('Organizacion', models.DO_NOTHING, db_column='id_Organizacion', blank=True, null=True)  # Field name made lowercase.
    id_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Casa'


class Categoriaproducto(models.Model):
    id_categoriaproducto = models.AutoField(db_column='id_categoriaProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CategoriaProducto'


class Detallecasausuario(models.Model):
    id_detallecasausuario = models.AutoField(db_column='id_detalleCasaUsuario', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleCasaUsuario'


class Detalleoferta(models.Model):
    id_detalleoferta = models.AutoField(db_column='id_detalleOferta', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_oferta = models.ForeignKey('Oferta', models.DO_NOTHING, db_column='id_oferta', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_estadooferta = models.ForeignKey('Estadooferta', models.DO_NOTHING, db_column='id_estadoOferta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetalleOferta'


class Detallepedido(models.Model):
    id_detallepedido = models.AutoField(db_column='id_detallePedido', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_estadopedido = models.ForeignKey('Estadopedido', models.DO_NOTHING, db_column='id_estadoPedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetallePedido'


class Detallestockproducto(models.Model):
    id_detallestockproducto = models.AutoField(db_column='id_detalleStockProducto', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    id_stock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='id_stock', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleStockProducto'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Direccion'


class Estadooferta(models.Model):
    id_estadooferta = models.AutoField(db_column='id_estadoOferta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoOferta'


class Estadopedido(models.Model):
    id_estadopedido = models.AutoField(db_column='id_estadoPedido', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoPedido'


class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    horavencimiento = models.TimeField(db_column='horaVencimiento', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Oferta'


class Organizacion(models.Model):
    id_organizacion = models.AutoField(db_column='id_Organizacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organizacion'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateField(db_column='fechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    horavencimiento = models.TimeField(db_column='horaVencimiento', blank=True, null=True)  # Field name made lowercase.
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pedido'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_categoriaproducto = models.ForeignKey(Categoriaproducto, models.DO_NOTHING, db_column='id_categoriaProducto', blank=True, null=True)  # Field name made lowercase.
    id_unidadmedida = models.ForeignKey('Unidadmedida', models.DO_NOTHING, db_column='id_unidadMedida', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stock'


class Tipodocumento(models.Model):
    id_tipodocumento = models.AutoField(db_column='id_tipoDocumento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoDocumento'


class Tipousuario(models.Model):
    id_tipousuario = models.AutoField(db_column='id_tipoUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoUsuario'


class Transporte(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    patente = models.CharField(max_length=20, blank=True, null=True)
    kilometraje = models.IntegerField(blank=True, null=True)
    estadoitv = models.CharField(db_column='estadoITV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anio = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_organizacion = models.ForeignKey(Organizacion, models.DO_NOTHING, db_column='id_Organizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transporte'


class Unidadmedida(models.Model):
    id_unidadmedida = models.AutoField(db_column='id_unidadMedida', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UnidadMedida'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contrasenia = models.CharField(max_length=255, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)
    id_tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='id_tipoUsuario', blank=True, null=True)  # Field name made lowercase.
    id_tipodocumento = models.ForeignKey(Tipodocumento, models.DO_NOTHING, db_column='id_tipoDocumento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'
