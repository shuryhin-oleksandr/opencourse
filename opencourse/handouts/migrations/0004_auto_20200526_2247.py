# Generated by Django 3.0.5 on 2020-05-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handouts', '0003_auto_20200526_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='is_active',
            new_name='accepted',
        ),
        migrations.AlterField(
            model_name='handout',
            name='attachment',
            field=models.FileField(upload_to='handouts/%Y-%m-%d/'),
        ),
        migrations.AlterField(
            model_name='handout',
            name='name',
            field=models.CharField(default=None, max_length=40),
            preserve_default=False,
        ),
    ]