# Generated by Django 5.0.6 on 2024-06-11 13:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriaproducto',
            fields=[
                ('id_categoriaproducto', models.AutoField(db_column='id_categoriaProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'CategoriaProducto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detallecasausuario',
            fields=[
                ('id_detallecasausuario', models.AutoField(db_column='id_detalleCasaUsuario', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('fechaingreso', models.DateField(blank=True, db_column='fechaIngreso', null=True)),
            ],
            options={
                'db_table': 'DetalleCasaUsuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalleoferta',
            fields=[
                ('id_detalleoferta', models.AutoField(db_column='id_detalleOferta', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DetalleOferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detallepedido',
            fields=[
                ('id_detallepedido', models.AutoField(db_column='id_detallePedido', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DetallePedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detallestockproducto',
            fields=[
                ('id_detallestockproducto', models.AutoField(db_column='id_detalleStockProducto', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DetalleStockProducto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('calle', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadooferta',
            fields=[
                ('id_estadooferta', models.AutoField(db_column='id_estadoOferta', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'EstadoOferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadopedido',
            fields=[
                ('id_estadopedido', models.AutoField(db_column='id_estadoPedido', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'EstadoPedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateField(blank=True, db_column='fechaInicio', null=True)),
                ('horainicio', models.TimeField(blank=True, db_column='horaInicio', null=True)),
                ('fechavencimiento', models.DateField(blank=True, db_column='fechaVencimiento', null=True)),
                ('horavencimiento', models.TimeField(blank=True, db_column='horaVencimiento', null=True)),
            ],
            options={
                'db_table': 'Oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id_organizacion', models.AutoField(db_column='id_Organizacion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Organizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateField(blank=True, db_column='fechaInicio', null=True)),
                ('horainicio', models.TimeField(blank=True, db_column='horaInicio', null=True)),
                ('fechavencimiento', models.DateField(blank=True, db_column='fechaVencimiento', null=True)),
                ('horavencimiento', models.TimeField(blank=True, db_column='horaVencimiento', null=True)),
            ],
            options={
                'db_table': 'Pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipodocumento',
            fields=[
                ('id_tipodocumento', models.AutoField(db_column='id_tipoDocumento', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'TipoDocumento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipousuario',
            fields=[
                ('id_tipousuario', models.AutoField(db_column='id_tipoUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'TipoUsuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id_transporte', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, max_length=255, null=True)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('patente', models.CharField(blank=True, max_length=20, null=True)),
                ('kilometraje', models.IntegerField(blank=True, null=True)),
                ('estadoitv', models.CharField(blank=True, db_column='estadoITV', max_length=255, null=True)),
                ('anio', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidadmedida',
            fields=[
                ('id_unidadmedida', models.AutoField(db_column='id_unidadMedida', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'UnidadMedida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id_casa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('id_direccion', models.ForeignKey(blank=True, db_column='id_direccion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProntaEntregaApp.direccion')),
                ('id_organizacion', models.ForeignKey(blank=True, db_column='id_Organizacion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProntaEntregaApp.organizacion')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUsuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('nombreusuario', models.CharField(blank=True, db_column='nombreUsuario', max_length=255, null=True, unique=True)),
                ('documento', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('genero', models.IntegerField(blank=True, choices=[(0, 'Hombre'), (1, 'Mujer'), (2, 'Prefiero no decirlo')], null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='usuarios/')),
                ('fechaUnion', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('id_direccion', models.ForeignKey(blank=True, db_column='id_direccion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProntaEntregaApp.direccion')),
                ('id_tipodocumento', models.ForeignKey(blank=True, db_column='id_tipoDocumento', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProntaEntregaApp.tipodocumento')),
                ('id_tipousuario', models.ForeignKey(blank=True, db_column='id_tipoUsuario', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProntaEntregaApp.tipousuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Usuario',
                'managed': True,
            },
        ),
    ]
