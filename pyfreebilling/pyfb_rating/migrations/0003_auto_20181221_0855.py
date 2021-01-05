# Generated by Django 2.1.4 on 2018-12-21 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_company', '0004_auto_20181210_1138'),
        ('pyfb_rating', '0002_auto_20181207_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='providerratecard',
            options={'ordering': ('provider', 'name')},
        ),
        migrations.AddField(
            model_name='providerratecard',
            name='provider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='providers', to='pyfb_company.Provider', verbose_name='Provider'),
            preserve_default=False,
        ),
    ]
