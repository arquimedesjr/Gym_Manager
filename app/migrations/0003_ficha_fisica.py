# Generated by Django 3.0.4 on 2020-04-02 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200330_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha_fisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medida_costas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_peito', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_abdome', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_tricpes', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_biceps', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_antibraco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_coxa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_panturrilha', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('medida_peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Aluno')),
            ],
        ),
    ]