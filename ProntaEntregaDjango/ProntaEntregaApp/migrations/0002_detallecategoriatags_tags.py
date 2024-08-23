from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProntaEntregaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detallecategoriatags',
            fields=[
                ('id_detallecategoriatags', models.AutoField(db_column='id_detalleCategoriaTags', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'DetalleCategoriaTags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id_tags', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Tags',
                'managed': False,
            },
        ),
    ]
