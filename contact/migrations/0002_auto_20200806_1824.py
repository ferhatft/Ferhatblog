# Generated by Django 3.0.5 on 2020-08-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('Anahtar Teslim Web Sitesi', 'Anahtar Teslim Web Sitesi'), ('HTML5 CSS3', 'HTML5 CSS3'), ('Sıfırdan Tema', 'Sıfırdan Tema'), ('SEO Uygulaması', 'SEO Uygulaması'), ('Diğer', 'Diğer'), ('Talebiniz', 'Talebiniz')], default='Talebiniz', max_length=50),
        ),
    ]