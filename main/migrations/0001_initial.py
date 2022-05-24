# Generated by Django 4.0.4 on 2022-05-04 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('valor', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('cpf', models.CharField(max_length=15)),
                ('nascimento', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=80)),
                ('fone', models.CharField(blank=True, max_length=15, null=True)),
                ('ativo', models.BooleanField(default=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=main.models.upload_image_user)),
                ('idAssinaturaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assinatura', to='main.assinatura')),
                ('idUserFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('descricao', models.CharField(max_length=300)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=main.models.upload_image_movie)),
                ('idCategoriaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='main.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFilmeFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filmes', to='main.filmes')),
                ('idUsuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='main.usuarios')),
            ],
        ),
    ]
