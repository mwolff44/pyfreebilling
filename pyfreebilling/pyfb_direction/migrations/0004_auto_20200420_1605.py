# Generated by Django 2.1.7 on 2020-04-20 16:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_direction', '0003_auto_20190327_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Risk evaluation')),
            ],
            options={
                'db_table': 'pyfb_direction_risk',
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='country',
            name='risk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyfb_direction.Risk', verbose_name='risk evaluation'),
        ),
    ]
