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
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleCasaUsuario'


class Detalleofertaproducto(models.Model):
    id_detalleofertaproducto = models.AutoField(db_column='id_detalleOfertaProducto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_oferta = models.ForeignKey('Oferta', models.DO_NOTHING, db_column='id_oferta', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_estadoproductooferta = models.ForeignKey('Estadoproductooferta', models.DO_NOTHING, db_column='id_estadoProductoOferta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetalleOfertaProducto'


class Detallepedidoproducto(models.Model):
    id_detallepedidoproducto = models.AutoField(db_column='id_detallePedidoProducto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_estadoproductopedido = models.ForeignKey('Estadoproductopedido', models.DO_NOTHING, db_column='id_estadoProductoPedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetallePedidoProducto'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Direccion'


class Estadoproductooferta(models.Model):
    id_estadoproductooferta = models.AutoField(db_column='id_estadoProductoOferta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoProductoOferta'


class Estadoproductopedido(models.Model):
    id_estadoproductopedido = models.AutoField(db_column='id_estadoProductoPedido', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadoProductoPedido'


class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Oferta'


class Organizacion(models.Model):
    id_organizacion = models.AutoField(db_column='id_Organizacion', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organizacion'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
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


class Stockproducto(models.Model):
    id_stockproducto = models.AutoField(db_column='id_stockProducto', primary_key=True)  # Field name made lowercase.
    id_casa = models.ForeignKey(Casa, models.DO_NOTHING, db_column='id_casa', blank=True, null=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StockProducto'


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
    anio = models.DateTimeField(blank=True, null=True)
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
    dni = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)
    id_tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='id_tipoUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
