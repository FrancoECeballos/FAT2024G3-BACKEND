# Generated by Django 5.0.6 on 2024-05-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProntaEntregaApp', '0001_initial'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Detalleofertaproducto',
        ),
        migrations.DeleteModel(
            name='Detallepedidoproducto',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Estadoproductooferta',
        ),
        migrations.DeleteModel(
            name='Estadoproductopedido',
        ),
        migrations.DeleteModel(
            name='Stockproducto',
        ),
    ]