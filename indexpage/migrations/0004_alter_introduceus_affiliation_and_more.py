# Generated by Django 4.0.3 on 2022-03-09 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0003_introduceus_category_alter_publicationsyears_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduceus',
            name='Affiliation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='introduceus',
            name='category',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Research Professor', 'Research Professor'), ('MS Students', 'MS Students'), ('Undergraduate', 'Undergraduate'), ('Research Collaborators', 'Research Collaborators'), ('PhD Students', 'PhD Students')], max_length=40),
        ),
        migrations.AlterField(
            model_name='publicationsyears',
            name='year',
            field=models.CharField(choices=[('2015', 2015), ('2017', 2017), ('2019', 2019), ('2022', 2022), ('2023', 2023), ('2018', 2018), ('2021', 2021), ('2016', 2016), ('2020', 2020)], max_length=30, unique=True),
        ),
    ]
